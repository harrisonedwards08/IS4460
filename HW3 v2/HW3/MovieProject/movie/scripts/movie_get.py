import requests

id = 1

api_url = 'http://127.0.0.1:8000/api/movies/'

response = requests.get(api_url)


if response.status_code == 200:
    movie_data = response.json()
    print(movie_data)
else:
    print("Error retrieving movie")
    print(f"Status code: {response.status_code}")

