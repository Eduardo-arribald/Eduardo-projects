import re
import sys


def main():
    #print(count(input("Text: ")))
    x = "um"
    print(count(x))

def count(s):
    return len(re.findall(r"\Wum\W", s))


if __name__ == "__main__":
    main()
