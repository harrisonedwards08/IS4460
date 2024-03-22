import requests
import json

id = 1

api_url = f'http://localhost:8000/api/customers/{id}/'

customer_data = {

    'name': 'Customer Z',
    'email': 'customerz@example.com',
    'phone_number': '1112223333'

}

response = requests.put(api_url, data = json.dumps(customer_data), headers = {'Content-Type':'application/json'})


if response.status_code == 200:
    print("customer updated")

else:
    print("error updating customer")

