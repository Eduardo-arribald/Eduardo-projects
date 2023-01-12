
import sys
import requests
import json

def main():
    try:
        if len(sys.argv) == 2 and sys.argv[1].isdigit():
            x = float(sys.argv[1])
            bitcoin = get_price(x)
            print(f"${round(bitcoin, 4)}")
        elif len(sys.argv) < 2:
            print("Missing command-line argument")
            sys.exit()
        else:
            print("Command-line argument is not a number")
            sys.exit()
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit()

def get_price(n:float):
    try:
        price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        p = json.dumps(price.json(), indent= 2)
        dictionary = price.json()
        bpi = dictionary["bpi"]
        usd = bpi["USD"]
        price = float(usd["rate_float"])
        usd_price = price*n
        return usd_price
    except requests.RequestException:
        print("Problema Request")


main()