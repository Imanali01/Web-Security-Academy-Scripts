## URL-based access control can be circumvented
### Lab Scenario
This website has an unauthenticated admin panel at `/admin`, but a front-end system has been configured to block external access to that path. However, the back-end application is built on a framework that supports the `X-Original-URL` header.
To solve the lab, access the admin panel and delete the user `carlos`.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/access-control/lab-url-based-access-control-can-be-circumvented`.
2. Run `python3 script.py <your lab URL>`. The script will delete the user `carlos` and solve the lab.