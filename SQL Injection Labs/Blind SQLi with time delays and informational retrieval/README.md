## Blind SQL injection with time delays and information retrieval
### Lab Scenario
This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.
The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows or causes an error. However, since the query is executed synchronously, it is possible to trigger conditional time delays to infer information.
The database contains a different table called `users`, with columns called `username` and `password`. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.
To solve the lab, log in as the `administrator` user.

### Instructions
To solve this lab using the script:
1. Access lab here: `https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval`
2. Run `python3 script.py <your lab url>`
   This script will successfully exploit the application's time based SQL injection vulnerability retrieve the `administrator` user's password.