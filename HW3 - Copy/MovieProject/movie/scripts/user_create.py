import requests
import json

user_data = {
    'username':'hed',
    'password':'vrysecure',
    'first_name': 'hank',
    'last_name':'tank',
    'email': 'hank@email.com'
}

api_url = 'http://127.0.0.1:8000/api/users/'

response = requests.post(api_url,data = json.dumps(user_data),headers= {'Content-Type':'application/json'})

if response.status_code == 201:
    print("User created")
else:
    print("Error creating user")
    print(f"Status code: {response.status_code}")
