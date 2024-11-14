## Parameter cloaking
### Lab Scenario
This lab is vulnerable to web cache poisoning because it excludes a certain parameter from the cache key. There is also inconsistent parameter parsing between the cache and the back-end. A user regularly visits this site's home page using Chrome.
To solve the lab, use the parameter cloaking technique to poison the cache with a response that executes `alert(1)` in the victim's browser.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/web-cache-poisoning/exploiting-implementation-flaws/lab-web-cache-poisoning-param-cloaking`.
2. Run `python3 script.py <your lab URL>`. The script will solve the lab and cause `alert(1)` to execute in the visitor's browser. If you refresh the page after running the script, you should see the alert box appear.