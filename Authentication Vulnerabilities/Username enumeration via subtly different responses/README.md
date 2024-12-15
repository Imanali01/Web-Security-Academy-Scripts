## Username enumeration via subtly different responses
### Lab Scenario
This lab is subtly vulnerable to username enumeration and password brute-force attacks. It has an account with a predictable username and password, which can be found in the following wordlists:
- <a href="https://portswigger.net/web-security/authentication/auth-lab-usernames">Candidate usernames </a>
- <a href="https://portswigger.net/web-security/authentication/auth-lab-passwords">Candidate passwords </a>

To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.

### Instructions
To solve the lab using this script:
1. Access the lab here: `https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-subtly-different-responses`
2. Run `python3 script.py <your lab URL>`
