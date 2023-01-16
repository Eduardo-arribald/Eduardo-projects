
#data = (''.join(input("Fraction: ").split())).split("/")

#print(data)

#x = int(data[0])
#y = int(data[2])
#print(x/y)


def main():
    n = input("Fraction: ")
    w = convert(n)
    print(w)
    print(gauge(w))


def convert(fraction):
    print(fraction.split())
    fraction = (''.join(fraction.split())).split("/")
    data = fraction
    x = int(data[0])
    y = int(data[1])
    if x > y:
        return ValueError
    else:
        return(int(100*round(x/y, 2)))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif 99 <= percentage == 100:
        return "F"
    elif 1 < percentage < 99:
        return f"{percentage}%"


"""
def fuel():
    while True:
        try:
            data = (''.join(input("Fraction: ").split())).split("/")
            x = int(data[0])
            y = int(data[1])
            #print(x/y)
            if x/y <= .01:
                print("E")
            elif 1 >= x/y >= .99:
                print("F")
            elif x/y > 1:
                continue
            else:
                print(str(int(100*round(x/y, 2)))+"%")
            break
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
"""

if __name__=="__main__":
    main()
