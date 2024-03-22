import requests

id = 1

api_url = 'http://localhost:8000/api/orders/'
response = requests.get(api_url)

if response.status_code == 200:
    order_data = response.json()
    print(order_data)

else:
    print("error retrieving order")