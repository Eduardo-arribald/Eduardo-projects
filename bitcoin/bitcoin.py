
import sys
import requests
import json

try:
    x = input("Request: ")
    x = float(x)
    price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    p = json.dumps(price.json(), indent= 2)
    dictionary = price.json()
    print(price)
    print(p)
    for 

except requests.RequestException:
    print("Problema Request")


    #{"time":{"updated":"Jan 11, 2023 23:40:00 UTC","updatedISO":"2023-01-11T23:40:00+00:00","updateduk":"Jan 11, 2023 at 23:40 GMT"},"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin","bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"17,888.0105","description":"United States Dollar","rate_float":17888.0105},"GBP":{"code":"GBP","symbol":"&pound;","rate":"14,947.0785","description":"British Pound Sterling","rate_float":14947.0785},"EUR":{"code":"EUR","symbol":"&euro;","rate":"17,425.5339","description":"Euro","rate_float":17425.5339}}}

#Excepts breaks the program if the input isn't a number.
except ValueError:
    print("Problema Request")
    sys.exit()