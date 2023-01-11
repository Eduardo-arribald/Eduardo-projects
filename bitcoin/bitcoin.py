
import sys
import requests
import json

try:

    x = input("Request: ")
    x = float(x)
    price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    p = json.dumps(price.json(), indent= 2)
    dictionary = price.json()
        #print(price)
        #print(p)
        bpi = dictionary["bpi"]
        usd = bpi["USD"]
        price = usd["rate_float"]
        print(price)

except requests.RequestException:
    print("Problema Request")

#Excepts breaks the program if the input isn't a number.
except ValueError:
    print("Command-line argument is not a number")
    sys.exit()

def 