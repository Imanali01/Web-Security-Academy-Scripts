## Blind OS command injection with output redirection
### Lab Scenario
This lab contains a blind OS command injection vulnerability in the feedback function.
The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response. However, you can use output redirection to capture the output from the command. There is a writable folder at:

```
/var/www/images/
```
The application serves the images for the product catalog from this location. You can redirect the output from the injected command to a file in this folder, and then use the image loading URL to retrieve the contents of the file.
To solve the lab, execute the `whoami` command and retrieve the output.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/os-command-injection/lab-blind-output-redirection`.
2. Run `python3 script.py <your lab URL>`. The script will execute the `whoami` command, redirect the output to a file, and retrieve the contents of the file.