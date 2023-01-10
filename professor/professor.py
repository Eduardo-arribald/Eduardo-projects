
import random

def main():
    a = get_level()
    x = generate_integer(a)
    y = generate_integer(a)
    solved = 0
    wrongs = 0
    tries = 0
    #Here is where the loop should begin.
    while True:
        answer = input(f"{x} + {y} =")
        if answer.isdigit() and tries < 3:
            answer = int(answer)
            if answer == (x + y):
                tries = 0
                solved += 1
                x = generate_integer(a)
                y = generate_integer(a)
            elif answer != (x + y):
                print("EEE")
                tries += 1
                wrongs += 1
                if tries == 3:
                    print(f"{x} + {y} =", str(x+y))
                    x = generate_integer(a)
                    y = generate_integer(a)
                    wrongs += 1
            #Check if 10 problems were solved
            if (solved + wrongs) == 10:
                break
        elif tries == 3:
            x = generate_integer(a)
            y = generate_integer(a)
            wrongs += 1
            print("EEE")
        elif (solved + wrongs) == 10:
            print(f"Your score is: {solved/10}")
            break
        else:
            print("EEE")
            tries += 1


def get_level():
    while True:
        try:
            #Check if users input a number in the range
            n = input("Level: ")
            n = int(n)
            if n in range(1,4):
                return n
        except:
            print("error")
            break


def generate_integer(x):
    if x in [1, 2, 3]:
        x = random.randint(1, (int("1"*x)*9))
        return x
    else:
        return ValueError



if __name__ == "__main__":
    main()



