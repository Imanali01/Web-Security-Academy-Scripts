## Web shell upload via extension blacklist bypass
### Lab Scenario
This lab contains a vulnerable image upload function. Certain file extensions are blacklisted, but this defense can be bypassed due to a fundamental flaw in the configuration of this blacklist.
To solve the lab, upload a basic PHP web shell, then use it to exfiltrate the contents of the file `/home/carlos/secret`. Submit this secret using the button provided in the lab banner.
You can log in to your own account using the following credentials: `wiener:peter`

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-extension-blacklist-bypass`.
2. Run `python3 script.py <your lab URL>` The script will display the contents of the `/home/carlos/secret` file.