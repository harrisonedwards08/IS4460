import requests

id = 1

api_url = f'http://localhost:8000/api/customers/{id}/'


response = requests.delete(api_url)

if response.status_code == 204:
    print("customer deleted")
else:
    print("error")