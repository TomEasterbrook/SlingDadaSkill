from constants import BASE
from datetime import *
from os.path import exists

import requests


'''A quick and dirty method for athing with the Sling API. Returns header dict for subsequent quires  '''


# TODO: Add redundancy for if auth fails
# TODO: Save header for use for up to 30 days

def login_with_credentials():
    while True:
        email = input("Please enter your email address")
        password = input("Please enter your password")
        auth_dict = {'email': email, "password": password}
        auth_req = requests.post(BASE + "account/login", json=auth_dict)

        if auth_req.status_code == 200:
            auth_code = auth_req.headers['authorization']
            save_auth_to_file(auth_code)
            print(auth_code)
            return {'authorization ': auth_code}
        else:
            print("Auth failed - Please try again \n ---------------------")


def save_auth_to_file(code_to_save):
    with open('session.txt', 'w') as file:
        file.write(datetime.today().date().isoformat() + " " + code_to_save)
        file.close()
    print("Your session has been saved for 30 days")


def auth_with_saved_session():
    session_data = extract_data_from_file()
    if is_session_vaild(session_data['created']):
        print(session_data['code'])
        print("Successfully loaded past session data  ")
        return {'authorization ': session_data['code']}
    else:
        print("Your saved session has expired - redirecting to login")
        return login_with_credentials()


def is_session_vaild(date_of_session):
    created_date = datetime.fromisoformat(date_of_session)
    expiry_date = created_date + timedelta(days=30)
    return expiry_date > datetime.today()


def extract_data_from_file():
    file = open("session.txt", 'r')
    raw_data = file.readline()
    file.close()
    parts = raw_data.split(" ")
    saved_session_dict = {"created": parts[0], "code": parts[1]}
    return saved_session_dict


def auth_with_sling():
    if exists("session.txt"):
        return auth_with_saved_session()
    else:
        return login_with_credentials()
