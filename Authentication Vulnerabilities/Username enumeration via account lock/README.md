## Username enumeration via account lock
### Lab Scenario
This lab is vulnerable to username enumeration. It uses account locking, but this contains a logic flaw. To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.
- <a href="https://portswigger.net/web-security/authentication/auth-lab-usernames">Candidate usernames </a>
- <a href="https://portswigger.net/web-security/authentication/auth-lab-passwords">Candidate passwords </a>

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-account-lock`
2. Run `python3 script.py <your lab URL>`