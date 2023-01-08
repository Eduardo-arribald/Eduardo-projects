
#data = (''.join(input("Fraction: ").split())).split("/")

#print(data)

#x = int(data[0])
#y = int(data[2])
#print(x/y)

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
                print(str(int(100*x/y))+"%")
            break
        except ZeroDivisionError:
            pass
        except ValueError:
            pass

fuel()
