import requests
import json

id = 1

api_url = f'http://localhost:8000/api/orders/{id}/'

order_data = {

    'customer':1,
    'order_total': '21.99',
    'notes': 'price went up'

}

response = requests.put(api_url, data = json.dumps(order_data), headers = {'Content-Type':'application/json'})


if response.status_code == 200:
    print("order updated")

else:
    print("error updating order")

