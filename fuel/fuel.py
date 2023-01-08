

def fuel():
    while True:
        try:
            data = list(''.join(input("Fraction: ").split()))
            x = int(data[0])
            y = int(data[2])
            if x/y <= .01:
                print("E")
            elif x/y >= .99:
                print("F")
            else:
                print(str(x/y)+"%")
            break
        except ZeroDivisionError:
            continue
        except ValueError:
            continue

fuel()
