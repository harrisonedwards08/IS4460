import requests
import json


api_url = 'http://localhost:8000/api/customers/'

customer_data = {
    'name':'Customer X',
    'email': 'customerx@email.com',
    'phone_number': '1112223333'
}




response = requests.post(url = api_url,
                         data = json.dumps(customer_data),
                         headers = {'Content-Type':'application/json'}
)


if response.status_code == 201:
    print("Customer created successfully")
else:
    print(f"Error")