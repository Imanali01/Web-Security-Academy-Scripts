## Visible error-based SQL injection
### Lab Scenario
This lab contains a SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie. The results of the SQL query are not returned.
The database contains a different table called users, with columns called username and password. To solve the lab, find a way to leak the password for the `administrator` user, then log in to their account.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/sql-injection/blind/lab-sql-injection-visible-error-based`.
2. Run `python3 script.py <your lab URL>`.
   This script will enumerate and display the password for the `administrator` user.
