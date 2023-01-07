
x, y, z = input("Expression: ").split(" ")

x, z = int(x), int(z)


def mats(x, y, z):
    match y:
        case "+":
            print(float(x + z))
        case "-":
            print(float(x - z))
        case "/":
            while True:
                if z != 0:
                    print(float(x / z))
                else:
                    print("Type ")
        case "*":
            print(float(x * z))
        case "^":
            print(float(x^z))

mats(x, y, z)

#print(x+z)

#print(type(z))

#print(type(x))

