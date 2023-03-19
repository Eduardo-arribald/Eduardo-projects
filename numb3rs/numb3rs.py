import re
import sys


def main():
    x = "127.0.0.1"
    #print(validate(input("IPv4 Address: ")))
    print(validate(x))


def validate(ip):
    #Maximum: 255
    y = re.search("\d[0-255]\.\d[0-255]\.\d[0-255]\.\d[0-255]", ip)
    if y:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
