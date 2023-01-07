
x, y, z = input("Expression: ").split(" ")

x, z = int(x), int(z)


def mats(x, y, z):
    match y:
        case "+":
            print(x + y)
        case "-":
            print(x - y)
        case "/":
            print(x / y)
        case "*":
            print(x * y)
        case "^":
            print("^")

mats(x, y, z)

#print(x+z)

#print(type(z))

#print(type(x))

