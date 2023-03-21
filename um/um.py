import re
import sys


def main():
    #print(count(input("Text: ")))
    x = "hola tum, asdasd" # 0
    x_1 = "um?" # 1
    x_2 = "yummy" # 0
    x_3 = "Um" # 1
    x_4 = "hola um, asdasd" # 1
    x_5 = "Um, thanks, um..." #2
    x_6 = "Um, thanks for the album."
    print(count(x))

def count(s):
    #s = str(s.lower())
    print(s)
    #print(len(list(s)))
    if " " in s:          #W\+
        match = re.findall(r"[^a-z]*um\W+", s, flags = re.IGNORECASE)
        return len(match)
    else:
        match = re.findall(r"um\W*", s, flags = re.IGNORECASE)

        return len(match)

if __name__ == "__main__":
    main()
