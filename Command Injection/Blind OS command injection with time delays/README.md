## Blind OS command injection with time delays
### Lab Scenario
This lab contains a blind OS command injection vulnerability in the feedback function.
The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response.
To solve the lab, exploit the blind OS command injection vulnerability to cause a 10 second delay.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/os-command-injection/lab-blind-time-delays`.
2. Run `python3 script.py <your lab URL>`. The script will exploit the application's command injection vulnerability and cause it to sleep for 10 seconds.