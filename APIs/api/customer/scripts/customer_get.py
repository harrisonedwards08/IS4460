import requests

id = 1

api_url = 'http://localhost:8000/api/customers/'
response = requests.get(api_url)

if response.status_code == 200:
    customer_data = response.json()
    print(customer_data)

else:
    print("error retrieving customer")