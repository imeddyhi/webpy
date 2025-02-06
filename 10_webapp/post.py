import requests
import json
import web

URI = "https://eddydemo-f3fa8-default-rtdb.firebaseio.com/personas.json"

# PUT data
data = {
    "013": {
        "nombre": "Eduardo",
        "apellido": "Caballero",
        "edad": 19
    }
}

response = requests.put(URI, json.dumps(data))
print(f"DATA: {data}")
print(f"HTTP Status Code: {response}")
print(f"Response: {response.text}")