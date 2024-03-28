import requests
import json

id = 1
api_url = f'http://127.0.0.1:8000/api/movies/{id}/'

movie_data = {

    'title':'even crazier movie',
    'description': 'this goes hard',
    'director':'twentin quarantino',
    'release_year': '2000',
    'budget':'1 million dollars',
    'runtime':'2 hours',
    'rating': 'R'

}


response = requests.put(api_url,data = json.dumps(movie_data),headers= {'Content-Type':'application/json'})

if response.status_code == 200:
    print("Movie updated")
else:
    print("Error updating movie")
    print(f"Status code: {response.status_code}")

