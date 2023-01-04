import requests
import json


URL =  "http://localhost:1234/employeeapi/"

########Get##############
def get_data(id =None):
    data ={}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.get(url = URL, headers=headers, data = json_data)
    data =r.json()
    print(data)
    
# get_data()

########create##############
def post_data():
    data ={
        "fullname": "gg",
        "emp_code": "2",
        "mobile": "9856321456"
    }

    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data)

    post_data()

# ######update##########

def updated_data():
    data = {
        "id":4, 
        "fullname":"vinay",
        "emp_code":"06",
        "mobile":"6958745214"
    }

    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.put(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data)

    # updated_data()


########delete##############
def delete_data():
    data = { "id":1 }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data)

    # delete_data()
