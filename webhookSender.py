import json
import requests

url = "http://localhost:8080/sell"

params = {
        "price": "1"
        }

resp = requests.post(url, json.dumps(params))
print(resp)
