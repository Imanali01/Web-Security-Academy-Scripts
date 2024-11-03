## Web cache poisoning with an unkeyed header
### Lab Scenario
This lab is vulnerable to web cache poisoning because it handles input from an unkeyed header in an unsafe way. 
An unsuspecting user regularly visits the site's home page. 
To solve this lab, poison the cache with a response that executes `alert(document.cookie)` in the visitor's browser.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-with-an-unkeyed-header`.
2. Run `python3 script.py <your lab URL>`. The script will solve the lab and cause `alert(document.cookie)` to execute in the visitor's browser. If you refresh the page after running the script, you should see the alert box appear.
