## SSRF with filter bypass via open redirection vulnerability
### Lab Scenario
This lab has a stock check feature which fetches data from an internal system.
To solve the lab, change the stock check URL to access the admin interface at `http://192.168.0.12:8080/admin` and delete the user `carlos`.
The stock checker has been restricted to only access the local application, so you will need to find an open redirect affecting the application first.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/ssrf/lab-ssrf-filter-bypass-via-open-redirection`.
2. Run `python3 script.py <your lab URL>`. The script will solve the lab and delete the user `carlos`.