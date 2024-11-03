## Targeted web cache poisoning using an unknown header
### Lab Scenario
This lab is vulnerable to web cache poisoning. A victim user will view any comments that you post. 
To solve this lab, you need to poison the cache with a response that executes `alert(document.cookie)` in the visitor's browser. 
However, you also need to make sure that the response is served to the specific subset of users to which the intended victim belongs.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-targeted-using-an-unknown-header`.
2. Run `python3 script.py <your lab URL>`. The script will solve the lab and cause `alert(document.cookie)` to execute in the victim's browser.