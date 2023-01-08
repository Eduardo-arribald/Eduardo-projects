

def fuel():
    #while True:
    try:

        data = list(''.join(input("Fraction: ").split()))
        x = int(data[0])
        y = int(data[2])
        print(str(x))
        print(str(y))
        if x/y <= .01:
            print("E")
        elif x/y >= .99:
            print("F")
        else:
            print(str(x/y)+"%")
        #break
    except ValueError:
        print("Not a number")

fuel()
