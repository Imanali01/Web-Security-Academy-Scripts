## Remote code execution via web shell upload
### Lab Scenario
This lab contains a vulnerable image upload function. It doesn't perform any validation on the files users upload before storing them on the server's filesystem.
To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file `/home/carlos/secret`. Submit this secret using the button provided in the lab banner.
You can log in to your own account using the following credentials: `wiener:peter`

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-web-shell-upload`
2. Run `python3 script.py <your lab url>` The script will display the contents of the `/home/carlos/secret file`.
