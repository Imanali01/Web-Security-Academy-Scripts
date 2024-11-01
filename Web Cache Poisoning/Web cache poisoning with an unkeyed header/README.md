## Web cache poisoning with an unkeyed header
### Lab Scenario
This lab is vulnerable to web cache poisoning because it handles input from an unkeyed header in an unsafe way. 
An unsuspecting user regularly visits the site's home page. 
To solve this lab, poison the cache with a response that executes `alert(document.cookie)` in the visitor's browser.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-with-an-unkeyed-header`.
2. Run `python3 script.py <your lab URL>`. The script will poison the web cache making it execute `alert(document.cookie)` in the victim's browser.
3. The lab will be marked as complete. Refresh your browser after running the script to confirm the alert box appears.