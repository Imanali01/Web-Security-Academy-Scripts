## File path traversal, traversal sequences stripped with superfluous URL-decode
### Lab Scenario
This lab contains a path traversal vulnerability in the display of product images.
The application blocks input containing path traversal sequences. It then performs a URL-decode of the input before using it.
To solve the lab, retrieve the contents of the `/etc/passwd` file.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/file-path-traversal/lab-superfluous-url-decode`.
2. Run `python3 script.py <your lab URL>`. The script will solve the lab and display the contents of the `/etc/passwd` file.