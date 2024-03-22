import requests
import json

api_url = 'http://127.0.0.1:8000/api/movies/'

movie_data = {

    'title':'crazy movie',
    'description': 'this goes hard',
    'director':'twentin quarantino',
    'release_year': '2000',
    'budget':'1 million dollars',
    'runtime':'2 hours',
    'rating': 'G'

}


response = requests.post(api_url,data = json.dumps(movie_data),headers= {'Content-Type':'application/json'})

if response.status_code == 201:
    print("Movie created")
else:
    print("Error creating movie")
    print(f"Status code: {response.status_code}")
