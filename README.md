# Load Testing using Locust

### Important Commands
Run Load Testing
~~~
Syntax:
locust -f PATH_TO_LOCUST_FILE --tags tag_name_here

Example:
locust -f ofd-backend/apis/v100/signup/locustfile.py --tags signup_api 
~~~

### Important Points
~~~
- Tag name is optional
- locust file name should be locustfile.py
~~~