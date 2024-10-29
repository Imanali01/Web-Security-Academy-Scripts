## File path traversal, validation of file extension with null byte bypass
### Lab Scenario
This lab contains a path traversal vulnerability in the display of product images.
The application validates that the supplied filename ends with the expected file extension.
To solve the lab, retrieve the contents of the `/etc/passwd` file.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/file-path-traversal/lab-validate-file-extension-null-byte-bypass`.
2. Run `python3 script.py <your lab URL>`. The script will solve the lab and display the contents of the `/etc/passwd` file.