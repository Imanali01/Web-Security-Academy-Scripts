## Basic SSRF against another back-end system
### Lab Scenario
This lab has a stock check feature which fetches data from an internal system.
To solve the lab, use the stock check functionality to scan the internal `192.168.0.X` range for an admin interface on port `8080`, then use it to delete the user `carlos`.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-backend-system`
2. Run `python3 script.py <your lab URL>` The script will solve the lab and delete the user `carlos`.