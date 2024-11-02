## Web cache poisoning with multiple headers
### Lab Scenario
This lab contains a web cache poisoning vulnerability that is only exploitable when you use multiple headers to craft a malicious request. A user visits the home page roughly once a minute. To solve this lab, poison the cache with a response that executes `alert(document.cookie)` in the visitor's browser.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-with-multiple-headers`.
2. Run `python3 script.py <your lab URL>`. The script will solve the lab by and cause `alert(document.cookie)` to execute in the visitor's browser. If you refresh the page after running the script, you should see the alert box appear.
