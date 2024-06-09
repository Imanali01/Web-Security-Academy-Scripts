## Blind SQL injection with conditional responses
### Lab Scenario
 This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.The results of the SQL query are not returned, and no error messages are displayed. But the application includes a "Welcome back" message in the page if the query returns any rows. The database contains a different table called users, with columns called username and password. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.
To solve the lab, log in as the administrator user. 

### Instructions
To solve this lab using the script:
1. Access lab here: `https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses`
2. Run `python3 script.py <your lab url>`
   This script will enumerate and display the password for the administrator user.
