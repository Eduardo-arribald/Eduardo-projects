
vars = input("Expression: ").split(" ")
x, y, z = vars[0], vars[1], vars[2]

print(vars)

def mats():
    while True:
        vars = input("Expression: ").split(" ")
        x, y, z = input("Expression: ").split(" ")
        x, z = int(x), int(z)
        match y:
            case "+":
                print(float(x + z))
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

#mats()

#print(x+z)

#print(type(z))

#print(type(x))

