import requests
import json
import os

api_key = os.getenv('grocy_api_key')

def input_function():
    barcode = input("barcode: ")
    location = input("location: ")
    price = input("price: ")

    return barcode,location,price

def purchase():
    barcode,location,price = input_function()
    url = "https://grocy.breadnet.co.uk/api/stock/products/by-barcode/"+ barcode +"/add"

    payload = json.dumps({
        "amount": 1,
        "best_before_date": "2019-01-19",
        "transaction_type": "purchase",
        "price": price,
        "location_id": location,
    })
    headers = {
        'accept': 'application/json',
        'GROCY-API-KEY': api_key,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    query = json.dumps(data)
    a = json.loads(query)
    transaction_id = a[0]["transaction_id"]
    print(transaction_id + "\n")

while True:
    purchase()
