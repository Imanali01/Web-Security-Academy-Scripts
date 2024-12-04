## Basic password reset poisoning
## Lab Scenario
This lab is vulnerable to password reset poisoning. The user `carlos` will carelessly click on any links in emails that he receives. To solve the lab, log in to Carlos's account.
You can log in to your own account using the following credentials: `wiener:peter`. Any emails sent to this account can be read via the email client on the exploit server.

### Instructions
To solve this lab using this script:
1. Access the lab here: `https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning/lab-host-header-basic-password-reset-poisoning`
2. Run `python3 script.py <your lab URL>`. The script will exploit the application's password reset poisoning vulnerability and solve the lab.