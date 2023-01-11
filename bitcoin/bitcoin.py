
import sys
import requests

try:
    x = input("Request: ")
    x = float(x)

except requests.RequestException or ValueError:
    print("Problema Request")

#Excepts breaks the program if the input isn't a number.
except ValueError:
    print("Problema Request")
    sys.exit()