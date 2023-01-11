
import random

def main():
    maximum_points = 10
    a = get_level()
    x = generate_integer(a)
    y = generate_integer(a)
    solved = 0
    wrongs = 0
    tries = 0
    #Here is where the loop should begin.
    while True:
        answer = input(f"{x} + {y} = ")
        if answer.isdigit() and tries < 3:
            answer = int(answer)
            if answer == (x + y):
                tries = 0
                solved += 1
                x = generate_integer(a)
                y = generate_integer(a)
            elif answer != (x + y):
                tries += 1
                #wrongs += 1
                if tries == 3:
                    print(f"{x} + {y} =", str(x+y))
                    x = generate_integer(a)
                    y = generate_integer(a)
                    wrongs += 1
                    tries = 0
                else:
                    print("EEE")

            #Check if 10 problems were solved
            if (solved + wrongs) == maximum_points:
                print(f"Score: {int(10*solved/maximum_points)}")
                print()
                break
        elif tries == 2 and (solved + wrongs) < maximum_points:
            #print("EEE")
            print(f"{x} + {y} =", str(x+y))
            x = generate_integer(a)
            y = generate_integer(a)
            wrongs += 1
            tries = 0

        elif (solved + wrongs) == maximum_points:
            #print(f"Score: {int(10*solved/maximum_points)}")
            print(f"Score: {int(solved)}")
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
        except ValueError:
            #print("error")
            pass


def generate_integer(x):
    if x == 1:
        x = random.randint(0, (int("1"*x)*9))
        return x
    elif x == 2:
        x = random.randint(10, (int("1"*x)*9))
        return x
    elif x == 3:
        x = random.randint(100, (int("1"*x)*9))
        return x
    else:
        return ValueError



if __name__ == "__main__":
    main()



