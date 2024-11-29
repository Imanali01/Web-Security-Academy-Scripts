## Weak isolation on dual-use endpoint
## Lab Scenario
This lab makes a flawed assumption about the user's privilege level based on their input. As a result, you can exploit the logic of its account management features to gain access to arbitrary users' accounts. To solve the lab, access the `administrator` account and delete the user `carlos`.
You can log in to your own account using the following credentials: `wiener:peter`.

### Instructions
To solve this lab using this script:
1. Access the lab here: `https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-weak-isolation-on-dual-use-endpoint`
2. Run `python3 script.py <your lab URL>`. The script will exploit the application's business logic vulnerability and solve the lab.