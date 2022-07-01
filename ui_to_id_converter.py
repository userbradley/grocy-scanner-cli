#!/usr/bin/env python3
import json
import os
import requests

api_key = os.getenv('grocy_api_key')
url = "https://grocy.breadnet.co.uk/api/objects/locations"

payload = json.dumps({
})

headers = {
    'accept': 'application/json',
    'GROCY-API-KEY': api_key,
    'Content-Type': 'application/json'
}
location = input("location name: ")
def search_for_id(location):
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()

    for k in data:
        if location == k['name']:
            return k['id']

if ":" in location:
    print(search_for_id(location))

else:
    print(location)



#print(search_for_id(location))
