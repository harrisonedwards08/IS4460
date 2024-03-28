import requests
id = 1


api_url = f'http://127.0.0.1:8000/api/users/{id}/'


response = requests.delete(api_url)
if response.status_code == 204:
    print("User deleted")
else:
    print("Error deleting user")
    print(f"Status code: {response.status_code}")