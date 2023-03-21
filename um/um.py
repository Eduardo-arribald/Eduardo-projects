import re
import sys


def main():
    #print(count(input("Text: ")))
    x = "hola um asdasd"
    x_1 = "um?"
    print(count(x_1))

def count(s):

    return len(re.findall(r"um\W", s))


if __name__ == "__main__":
    main()
