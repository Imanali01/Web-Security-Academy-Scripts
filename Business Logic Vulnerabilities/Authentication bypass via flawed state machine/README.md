## Authentication bypass via flawed state machine
## Lab Scenario
This lab makes flawed assumptions about the sequence of events in the login process. To solve the lab, exploit this flaw to bypass the lab's authentication, access the admin interface, and delete the user `carlos`.
You can log in to your own account using the following credentials: `wiener:peter`

### Instructions
To solve the lab using this script:
1. Access the lab here: `https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-authentication-bypass-via-flawed-state-machine`
2. Run `python3 script.py <your lab URL>`. The script will exploit the application's business logic vulnerability and solve the lab.