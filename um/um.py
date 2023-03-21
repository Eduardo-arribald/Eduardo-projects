import re
import sys


def main():
    #print(count(input("Text: ")))

    #I got this correct
    x = "um?" # 1
    x_1 = "yummy" # 0
    x_2 = "Um" # 1

    #I just need these too.
    x_3 = "hola tum, asdasd" # 0
    x_4 = "hola um, asdasd" # 1
    x_5 = "Um, thanks, um..." #2
    x_6 = "Um, thanks for the album." #1
    print(count(x_4))

def count(s):
    #s = str(s.lower())
    print(s)
    #print(len(list(s)))
    lista = s.split()
    print(lista)
    if " " in s:
        for i in lista:         #W\+
            match = re.findall(r"^[\W]*um[\W]*$", i, flags = re.IGNORECASE)
            #print(match)
            return len(match)
        
    else:
        match = re.findall(r"^\W?um\W?$", s, flags = re.IGNORECASE)
        return len(match)

if __name__ == "__main__":
    main()
