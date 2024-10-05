## SQL injection attack, listing the database contents on Oracle
### Lab Scenario
This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.
The application has a login function, and the database contains a table that holds usernames and passwords. You need to determine the name of this table and the columns it contains, then retrieve the contents of the table to obtain the username and password of all users.
To solve the lab, log in as the `administrator` user.



### Instructions
To solve this lab using the script:
1. Access lab here: `https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle`
2. Run `python3 script.py <your lab url>`
   This script will enumerate and display the password for the administrator user.