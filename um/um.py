import re
import sys


def main():
    #print(count(input("Text: ")))
    x = "hola um asdasd"
    print(count(x))

def count(s):
    return len(re.findall(r"^um$", s))


if __name__ == "__main__":
    main()
