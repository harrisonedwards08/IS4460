import requests

url = "http://127.0.0.1:8000/api/movies/?param=\'value\'"
resp = requests.get(url)
print(resp)