## User ID controlled by request parameter with password disclosure
### Lab Scenario
his lab has user account page that contains the current user's existing password, prefilled in a masked input.
To solve the lab, retrieve the administrator's password, then use it to delete the user `carlos`.
You can log in to your own account using the following credentials: `wiener:peter`.


### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-password-disclosure.
2. Run `python3 script.py <your lab URL>`. The script will solve the lab retrieving the administrator user's password, then using it to delete the user `carlos`.