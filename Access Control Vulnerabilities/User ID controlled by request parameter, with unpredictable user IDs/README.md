## User ID controlled by request parameter, with unpredictable user IDs
### Lab Scenario
This lab has a horizontal privilege escalation vulnerability on the user account page, but identifies users with GUIDs.
To solve the lab, find the GUID for `carlos`, then submit his API key as the solution.
You can log in to your own account using the following credentials: `wiener:peter`.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-unpredictable-user-ids`.
2. Run `python3 script.py <your lab URL>`. The script will retrieve carlos's API key and solve the lab.