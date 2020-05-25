import requests
import auth
from constants import BASE


def get_employee_data():
    global emp_data
    auth_header = auth.auth_with_sling()
    emp_req = requests.get(BASE + "/users", headers=auth_header)
    return emp_req.json()


def create_employee_reference_file(data):
    raw_emp_data = data
    emp_ref_file = open('employees.txt','w')
    for emp in raw_emp_data:
        if (emp['lastname'] != "Easterbrook") & emp['active'] == True:
            emp_ref_file.write(emp['name'] + " " + emp['lastname'] + " - " +str(emp['id'])+'\n')
    emp_ref_file.close()

def read_employee_reference_file():
    emp_list = []
    emp_ref_file = open('employees.txt','r')
    for line in emp_ref_file:
        entry = (line.strip().split(" - "))
        name_parts = entry[0].split(" ")
        id = entry[1]
        emp_list.append({'first':name_parts[0],'last':name_parts[1],'id':id})

    return emp_list

#create_employee_reference_file(get_employee_data())
list = read_employee_reference_file()

for emp in list:
    print(emp['first'])