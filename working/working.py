
import re
import sys


def main():
    x = "9:00 AM to 5:00 PM"
    x_1 = "9 AM to 5 PM"
    x_2 = "5:00 PM to 9:00 AM"
    x_3 = "9 AM to 5:30 PM"
    x_4 = "12:60 AM to 13:00 PM"
    convert(x_4)
    #print(convert(input("Hours: ")))

def convert(s):
    #w = re.search(r'"(?:http|https)://(?:www.)?youtube.com/embed/(\w+)"', s)
    w = re.search(r'(1[1-2]|[0-9]):?([0-5][0-9])? (AM|PM) ?[a-z]* ?(1[1-2]|[0-9]):?([0-5][0-9])? (AM|PM)', s)
    if w:
        print("Simon")
        print(w.group(1)) #hour
        print(w.group(2)) #minutes
        print(w.group(3)) #AM / PM
        hour_1 = int(w.group(1)) #hour
        #minute_1 = int(w.group(2)) #minutes (can be None)
        time_1 = w.group(3) #AM/PM
        hour_2 = int(w.group(4))
        #minute_2 = int(w.group(5))
        time_2 = w.group(6)
        if time_1 == "PM" and time_2 == "PM":
            hour_1 = hour_1+12
            hour_2 = hour_2+12
        



    else:
        print("Nel")


if __name__ == "__main__":
    main()

