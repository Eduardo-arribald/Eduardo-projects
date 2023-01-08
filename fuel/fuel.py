

def fuel():
    while True:
        data = list(''.join(input("Fraction: ").split()))
        n = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "/"]
        if data[0] or data[2] not in n:
            continue
        else:
            if int(data[0])/int(data[2]) <= .01:
                print("E")
            elif int(data[0])/int(data[2]) >= .99:
                print("F")
            else:
                print(str(int(data[0])/int(data[2])))
            break


fuel()
