
import re
import sys


def main():
    x = "9:00 AM to 5:00 PM"
    print(convert(x))
    #print(convert(input("Hours: ")))


def convert(s):
    #w = re.search(r'"(?:http|https)://(?:www.)?youtube.com/embed/(\w+)"', s)
    w = re.search(r'(1?[0-9]:[0-6][0-9]) [AM|PM] \w (1?[0-9]:[0-6][0-9]) [AM|PM]', s)



if __name__ == "__main__":
    main()

