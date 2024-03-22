import requests

id = 1

api_url = f'http://localhost:8000/api/orders/{id}/'

response = requests.delete(api_url)

if response.status_code == 204:
    print("order deleted")
else:
    print("error")