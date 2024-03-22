import requests
import json



api_url = 'http://localhost:8000/api/orders/'

order_data = {

    'customer': 1,
    'order_total': '15.99',
    'notes': "this ain't too bad"
    
}


response = requests.post(url = api_url,
                         data = json.dumps(order_data),
                         headers = {'Content-Type':'application/json'}
)


if response.status_code == 201:
    print("Order created successfully")
else:
    print(f"Error")