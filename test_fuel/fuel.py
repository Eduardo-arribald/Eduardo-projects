

def main():
    n = input("Fraction: ")
    w = convert(n)
    #print(w)
    print(gauge(w))


def convert(fraction):
    try:
        #print(fraction.split())
        fraction = (''.join(fraction.split())).split("/")
        data = fraction
        x = int(data[0])
        y = int(data[1])
        return(int(100*round(x/y, 2)))
    except ZeroDivisionError:
        pass
    except:
        pass


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    elif 1 < percentage < 99:
        return f"{percentage}%"
    else:
        return ValueError


if __name__=="__main__":
    main()
