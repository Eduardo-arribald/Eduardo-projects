import re
import sys


def main():
    #print(count(input("Text: ")))
    x = "hola um asdasd"
    x_1 = "um?"
    x_2 = "yummy"
    x_3 = "Um"
    print(count(x_3))

def count(s):
    s = str(s.lower())
    print(s)
    #w = len(re.findall(r"(um|Um)\W+", s, re.IGNORECASE))
    match = re.findall(r"um\W+", s, flags = re.IGNORECASE)

    #y = re.search()
    return len(match)

if __name__ == "__main__":
    main()
