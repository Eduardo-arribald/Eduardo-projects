
def mats():
    while True:
        x, y, z = input("Expression: ").split()
        x, z = int(x), int(z)
        match y:
            case "+":
                print(round(float(x + z), 1))
            case "-":
                print(round(float(x - z), 1))
            case "/":
                if z != 0:
                    print(round(float(x / z), 1))
                else:
                    continue
            case "*":
                print(round(float(x * z), 1))
            case "^":
                print(round(float(x^z), 1))
        break

mats()


