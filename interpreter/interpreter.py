
x, y, z = input("Expression: ").split(" ")

x, z = int(x), int(z)


def mats(x, y, z):
    match y:
        case "+":
            print("+")
        case "-":
            print("-")
        case "/":
            print("/")
        case "*":
            print("*")
        case "^":
            print("^")

mats(x, y, z)

#print(x+z)

#print(type(z))

#print(type(x))

