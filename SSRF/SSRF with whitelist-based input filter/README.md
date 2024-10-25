## SSRF with whitelist-based input filter
### Lab Scenario
This lab has a stock check feature which fetches data from an internal system.
To solve the lab, change the stock check URL to access the admin interface at `http://localhost/admin` and delete the user `carlos`.
The developer has deployed an anti-SSRF defense you will need to bypass.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/ssrf/lab-ssrf-with-whitelist-filter`.
2. Run `python3 script.py <your lab URL>`. The script will solve the lab and delete the user `carlos`.