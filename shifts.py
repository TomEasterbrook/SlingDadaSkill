import constants
import requests
import auth
import employee_data
import dates

emp_list = employee_data.read_employee_reference_file()
auth = auth.auth_with_sling()

for emp in emp_list:
    emp_req = requests.get(constants.BASE + "/calendar/"+constants.ORG_ID+"/users/"+emp['id'], headers=auth, params={'dates':dates.get_sample_timeframe()})
    print(emp_req.json())
    print(emp['id'])


