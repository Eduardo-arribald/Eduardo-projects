
def mats():
    while True:
        x, y, z = input("Expression: ").split()
        x, z = int(x), int(z)
        match y:
            case "+":
                print(float(x + z, 2))
                break
            case "-":
                print(float(x - z))
                break
            case "/":
                if z != 0:
                    print(float(x / z))
                    break
                else:
                    continue
            case "*":
                print(float(x * z))
                break
            case "^":
                print(float(x^z))
                break

mats()

#print(x+z)

#print(type(z))

#print(type(x))

