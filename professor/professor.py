
import random

def main():
    z = input("Level: ")
    get_level(z)


def get_level(n):
    n = int(n)
    if n in [1, 2, 3]:
        x = random.ranint(1, (int("1"*n)*9))



def generate_integer(level):
    ...


if __name__ == "__main__":
    main()



