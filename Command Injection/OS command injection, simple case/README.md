## OS command injection, simple case
### Lab Scenario
This lab contains an OS command injection vulnerability in the product stock checker.
The application executes a shell command containing user-supplied product and store IDs, and returns the raw output from the command in its response.
To solve the lab, execute the `whoami` command to determine the name of the current user.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/os-command-injection/lab-simple`.
2. Run `python3 script.py <your lab URL>`. The script will exploit the application's command injection vulnerability and return the response to the command `whoami`.