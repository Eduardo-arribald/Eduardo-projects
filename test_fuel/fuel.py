

def main():
    n = input()
    print(convert(n))
    #print(gauge(n))


def convert(fraction):
    try:
        #print(fraction.split())
        #split fraction to eliminate the spaces before and after the text.
        fraction = fraction.split()
        #print(fraction)
        fraction = (''.join(fraction)).split("/")
        data = fraction
        x = int(data[0])
        y = int(data[1])
        print(x)
        print(y)
        print(data)
        return(int(100*round(x/y, 2)))
    except ZeroDivisionError:
        pass
    except:
        pass


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif 98 < percentage <= 100:
        return "F"
    elif 1 < percentage < 99:
        return f"{percentage}%"
    else:
        return ValueError


if __name__=="__main__":
    main()
