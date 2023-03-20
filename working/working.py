
import re
import sys


def main():
    x = "9:00 AM to 5:00 PM"
    print(convert(x))
    #print(convert(input("Hours: ")))


def convert(s):
    w = re.search(r'"(?:http|https)://(?:www.)?youtube.com/embed/(\w+)"', s)
    w = re.search(r'', s)



if __name__ == "__main__":
    main()

