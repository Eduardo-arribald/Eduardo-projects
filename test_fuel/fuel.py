

def main():
    n = input('Fraction: ')
    n = convert(n)
    while True:
        n = gauge(n)
        if type(n) == int and int(n) > 100:
            continue
        else:
            print(n)


def convert(fraction):
    while True:
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
            #print(data)
            return (int(100*round(x/y, 2)))
        except ZeroDivisionError:
            pass
        except:
            pass
        else:
            break


def gauge(percentage):
    if float(percentage) <= 1:
        return "E"
    elif 98 < float(percentage) <= 100:
        return "F"
    elif 1 < float(percentage) < 99:
        return f"{percentage}%"
    else:
        return percentage


if __name__=="__main__":
    main()
