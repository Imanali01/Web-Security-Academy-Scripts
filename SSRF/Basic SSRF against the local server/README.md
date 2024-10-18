## Basic SSRF against the local server
### Lab Scenario
This lab has a stock check feature which fetches data from an internal system.
To solve the lab, change the stock check URL to access the admin interface at `http://localhost/admin` and delete the user `carlos`.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-localhost`.
2. Run `python3 script.py <your lab URL>`. The script will solve the lab and delete the user `carlos`.