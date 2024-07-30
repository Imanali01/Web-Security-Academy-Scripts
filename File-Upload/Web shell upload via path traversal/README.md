## Web shell upload via path traversal
### Lab Scenario
This lab contains a vulnerable image upload function. The server is configured to prevent execution of user-supplied files, but this restriction can be bypassed by exploiting a secondary vulnerability.
To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file `/home/carlos/secret`. Submit this secret using the button provided in the lab banner.
You can log in to your own account using the following credentials: `wiener:peter`

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-path-traversal`
2. Run `python3 script.py <your lab url>` The script will display the contents of the `/home/carlos/secret` file.
