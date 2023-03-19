import re
import sys


def main():
    x = "127.0.0.1"
    #x = "255."
    #print(validate(input("IPv4 Address: ")))
    print(validate(x))


def validate(ip):
    #Maximum: 255
    #y = re.search("^(([0-1]?[0-9]?[0-9]?|2[0-4][0-9]|25[0-5])\\.){3}([0-1]?[0-9]?[0-9]?|2[0-4][0-9]|25[0-5]){1}$", ip)
    y = re.search("^(2[0-5][0-5]|2[0-4][0-9]|1[0-9][0-9]?|[0-9][0-9]?)\.(2[0-5][0-5]|2[0-4][0-9]|1[0-9][0-9]?|[0-9][0-9]?)\.(2[0-5][0-5]|2[0-4][0-9]|1[0-9][0-9]?|[0-9][0-9]?)\.(2[0-5][0-5]|2[0-4][0-9]|1[0-9][0-9]?|[0-9][0-9]?)$", ip)
    if y:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
