from datetime import datetime
import json
import requests

BASE = "https://api.sling.is/v1/"

'''A quick and dirty method for athing with the Sling API. Returns header dict for subsequent quires  '''


# TODO: Add redundancy for if auth fails
# TODO: Save header for use for up to 30 days
def auth_with_sling():
    email = input("Please enter your email address")
    password = input("Please enter your email address")
    auth_dict = {'email': email, "password": password}
    auth_req = requests.post(BASE + "account/login", json=auth_dict)

    if auth_req.status_code == 200:
        return {'authorization ': auth_req.headers['authorization']}
    else:
        print("Auth failed - the program will now close")
        exit()


auth_header = auth_with_sling()
print(auth_header)
