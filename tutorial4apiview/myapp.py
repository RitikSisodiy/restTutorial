import requests
import json

URL = 'http://127.0.0.1:8000/student/'

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL , data = json_data)
    data = r.json()
    print(data)
def post_data():
    data = {
        'name':'nohit',
        'roll': 3534533,
        'city': 'ratlam',
    }
    headers = {'Content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL,headers = headers, data = json_data)
    data = r.json()
    print(data)
def update_data():
    data = {
        'name': 'dmahshdvadgg sfbsdfgs gsdg',
        'id' : 1,
        'roll' : '11111',
    }
    headers = {'Content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL,headers = headers,data = json_data)
    data = r.json()
    print(data)
def delete_data(id = None):
    if id is not None:
        data = {
            'id' : id,
        }
        headers = {'Content-Type':'application/json'}
        json_data = json.dumps(data)
        r = requests.delete(url=URL,headers = headers,data = json_data)
        data = r.json()
        print(data)
    else:
        print("passs the id for deletion")
get_data(3)
post_data()
# update_data()
# delete_data(3)