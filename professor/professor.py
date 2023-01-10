
import random

def main():
    get_level()
    


def get_level():
    while True:
        try:
            #Check if users input a number in the range
            n = input("Level: ")
            n = int(n)
            if n in range(1:4):
                return n
        except:
            print("error")
            break


def generate_integer(x):
    if x in [1, 2, 3]:
        x = random.ranint(1, (int("1"*x)*9))
        return x
    else:
        return ValueError



if __name__ == "__main__":
    main()



