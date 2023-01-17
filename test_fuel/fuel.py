

def main():
    n = input("Fraction: ")
    w = convert(n)
    #print(w)
    print(gauge(w))


def convert(fraction):
    #print(fraction.split())
    fraction = (''.join(fraction.split())).split("/")
    data = fraction
    x = int(data[0])
    y = int(data[1])
    if y == 0:
        return x / 0
    elif x > y:
        return ValueError
    else:
        return(int(100*round(x/y, 2)))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    elif 1 < percentage < 99:
        return f"{percentage}%"


if __name__=="__main__":
    main()
