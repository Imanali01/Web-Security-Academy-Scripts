## File path traversal, validation of start of path
### Lab Scenario
This lab contains a path traversal vulnerability in the display of product images.
The application transmits the full file path via a request parameter, and validates that the supplied path starts with the expected folder.
To solve the lab, retrieve the contents of the `/etc/passwd` file.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/file-path-traversal/lab-validate-start-of-path`.
2. Run `python3 script.py <your lab URL>`. The script will solve the lab and display the contents of the `/etc/passwd` file.