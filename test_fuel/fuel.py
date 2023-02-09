

def main():
    while True:
        n = input('Fraction: ')
        n = convert(n)
        n = gauge(n)
        if n == None or type(n) == int:
            continue
        elif n == ValueError:
            return ValueError
            break
        else:
            print(n)
            break


def convert(fraction):
    #while True:
        #try:
    #split fraction to eliminate the spaces before and after the text.
    fraction = fraction.split()
    fraction = (''.join(fraction)).split("/")
    data = fraction
    x = data[0]
    y = data[1]
    if y.isdigit() and x.isdigit() and int(x) <= int(y):
        x = int(x)
        y = int(y)
        #print(x)
        #print(y)
        #print(data)
        return (int(100*round(x/y, 2)))
    #else:
        #return ValueError
        #except ZeroDivisionError:
            #pass
        #except:

        #else:
            #break


def gauge(percentage):
    #print(type(percentage))
    #return percentage
    if type(percentage) == int:
        if float(percentage) <= 1:
            return "E"
        elif 98 < float(percentage) <= 100:
            return "F"
        elif 1 < float(percentage) < 99:
            return f"{percentage}%"
        else:
            #print("Es mayor a 100")
            ValueError
            #i = int('hola')
            #return percentage


if __name__=="__main__":
    main()
