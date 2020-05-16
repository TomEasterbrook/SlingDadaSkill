from datetime import *
import json
import requests
from os.path import exists

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
        auth_code = auth_req.headers['authorization']
        save_auth_to_file(auth_code)
        return {'authorization ': auth_code}
    else:
        print("Auth failed - the program will now close")
        exit()

def save_auth_to_file(code_to_save):
    with open('session.txt','w') as file:
        file.write(datetime.today().date().isoformat() + " " + code_to_save)
        file.close()
    print("Your session has been saved for 30 days")

def auth_with_saved_session():
    if check_expiry():
        print("yes")
    else:
        print('no')


def check_expiry():
    saved_session_dict = extract_data_from_file()
    created_date = datetime.fromisoformat(saved_session_dict['created'])
    expiry_date = created_date + timedelta(days=30)
    return expiry_date<datetime.today()



def extract_data_from_file():
    file = open("session.txt", 'r')
    raw_data = file.readline()
    file.close()
    parts = raw_data.split(" ")
    saved_session_dict = {"created": parts[0], "code": parts[1]}
    return saved_session_dict


if exists("session.txt"):
    auth_with_saved_session()
else:
    auth_with_sling()