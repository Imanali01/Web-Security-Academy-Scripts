## File path traversal, traversal sequences blocked with absolute path bypass
### Lab Scenario
This lab contains a path traversal vulnerability in the display of product images.
The application blocks traversal sequences but treats the supplied filename as being relative to a default working directory.
To solve the lab, retrieve the contents of the `/etc/passwd` file.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/file-path-traversal/lab-absolute-path-bypass`.
2. Run `python3 script.py <your lab URL>`. The script will solve the lab and display the contents of the `/etc/passwd` file.