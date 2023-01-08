

def fuel():
    while True:
        try:
            data = list(''.join(input("Fraction: ").split()))
            x = int(data[0])
            y = int(data[2])
            print(x/y)
            if data[1] != "/":
                print("mal")
                continue
            else:
                if x/y <= .01:
                    print("E")
                elif x/y >= .99:
                    print("F")
                else:
                    print(str(int(100*x/y))+"%")
                break
        except ZeroDivisionError:
            pass
        except ValueError:
            pass

fuel()
