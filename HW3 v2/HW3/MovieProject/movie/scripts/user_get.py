import requests

id = 1

api_url = 'http://127.0.0.1:8000/api/users/'

response = requests.get(api_url)


if response.status_code == 200:
    user_data = response.json()
    print(user_data)
else:
    print("Error retrieving user")
    print(f"Status code: {response.status_code}")

