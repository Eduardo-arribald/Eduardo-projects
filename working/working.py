
import re
import sys


def main():
    x = "9:00 AM to 5:00 PM"
    x_1 = "9 AM to 5 PM"
    x_2 = "5:00 PM to 9:00 AM"
    #print(convert(x))
    convert(x_2)
    #print(convert(input("Hours: ")))


def convert(s):
    #w = re.search(r'"(?:http|https)://(?:www.)?youtube.com/embed/(\w+)"', s)
    w = re.search(r'(1[1-2]|[0-9]):?([0-5][0-9]|60)? (AM|PM) ?[a-z]* ?(1[1-2]|[0-9]):?([0-5][0-9]|60)? (AM|PM)', s)
    if w:
        print("Simon")
        print(w.group(1))
        print(w.group(2))
        print(w.group(3))
    else:
        print("Nel")


if __name__ == "__main__":
    main()

