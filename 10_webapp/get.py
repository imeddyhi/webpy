import requests
import json
import web

URI = "https://eddydemo-f3fa8-default-rtdb.firebaseio.com/usuarios.json"

# GET data
response = requests.get(URI)

print(f"HTTP Status Code: {response}")
print(f"Response: {response.text}")