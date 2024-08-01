# client.py
import requests

for _ in range(10):
    response = requests.get("http://127.0.0.1:8000")
    print(response.text)