## Web cache poisoning with an unkeyed cookie
### Lab Scenario
This lab is vulnerable to web cache poisoning because cookies aren't included in the cache key. An unsuspecting user regularly visits the site's home page. To solve this lab, poison the cache with a response that executes `alert(1)` in the visitor's browser.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-with-an-unkeyed-cookie`.
2. Run `python3 script.py <your lab URL>`. The script will solve the lab and cause `alert(1)` to execute in the visitor's browser. If you refresh the page after running the script, you should see the alert box appear.
