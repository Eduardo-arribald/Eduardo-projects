

def main():
    g = input("Greet: ")
    print(value(g))


def value(greeting:str):
    greeting = greeting.lower().split()
    first = list(greeting[0])[0:5]
    hello = list("hello")
    if hello == first:
        return 0
    elif first[0]=="h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
