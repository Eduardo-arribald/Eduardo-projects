import re
import sys


def main():
    #print(count(input("Text: ")))
    x = "hola um asdasd"
    x:1
    print(count(x))

def count(s):
    return len(re.findall(r"\W[,.]*um[,.]*\W", s))


if __name__ == "__main__":
    main()
