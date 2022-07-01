import requests
import json
import os

api_key = os.getenv('grocy_api_key')

def input_function():
    location = input("location: ")


    url = "https://grocy.breadnet.co.uk/api/objects/locations"

    payload = json.dumps({
        })
    headers = {
        'accept': 'application/json',
        'GROCY-API-KEY': api_key,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    query = json.dumps(data)
    return query
    a = json.loads(query)

def search_location_id (location):
    query = input_function()
    for keyval in query:
        if location == keyval['name']:
            return keyval['id']
while True:
    search_location_id()
