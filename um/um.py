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
    #s = s.lower()
    return len(re.findall(r"um|Um\W+", s))


if __name__ == "__main__":
    main()
