## File path traversal, traversal sequences stripped non-recursively
### Lab Scenario
This lab contains a path traversal vulnerability in the display of product images.
The application strips path traversal sequences from the user-supplied filename before using it.
To solve the lab, retrieve the contents of the `/etc/passwd` file.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/file-path-traversal/lab-sequences-stripped-non-recursively`.
2. Run `python3 script.py <your lab URL>`. The script will solve the lab and display the contents of the `/etc/passwd` file.