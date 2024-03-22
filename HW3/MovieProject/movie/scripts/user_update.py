import requests
import json

id = 1
api_url = f'http://127.0.0.1:8000/api/users/{id}/'

user_data = {
    'username':'htank',
    'password':'moresecure',
    'first_name': 'hank',
    'last_name':'tank',
    'email': 'hank@email.com'
}



response = requests.put(api_url,data = json.dumps(user_data),headers= {'Content-Type':'application/json'})

if response.status_code == 200:
    print("User updated")
else:
    print("Error updating user")
    print(f"Status code: {response.status_code}")

