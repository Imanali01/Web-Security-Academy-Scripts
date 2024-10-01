## Blind SQL injection with time delays
### Lab Scenario
This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.
The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows or causes an error. However, since the query is executed synchronously, it is possible to trigger conditional time delays to infer information.
To solve the lab, exploit the SQL injection vulnerability to cause a 10 second delay.

### Instructions
To solve this lab using the script:
1. Access lab here: `https://portswigger.net/web-security/sql-injection/blind/lab-time-delays`
2. Run `python3 script.py <your lab url>`
   This script will solve the lab and inform you if the website is vulnerable to time based SQL injection.