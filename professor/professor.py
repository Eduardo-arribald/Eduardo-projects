
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
        #Check if tries are less than 3 and solved + wrongs are less than the total of problems.
        if tries < 3 and (solved + wrongs) < maximum_points:
            #Input your answer.
            answer = input(f"{x} + {y} = ")
            #Check if the user gave me a number.
            if answer.isdigit():
                #turn that number to int.
                answer = int(answer)
                #If answer is correct, reset tries and add 1 to "solved".
                #Generate new integers.
                if answer == (x + y):
                    tries = 0
                    solved += 1
                    x = generate_integer(a)
                    y = generate_integer(a)
                #If answer is incorrect, add 1 to tries.
                elif answer != (x + y):
                    tries += 1
                    #If tries are equal to 3 and the sum of solved and wrongs are less
                    #than the total of problems, print the answer, generate new numbers
                    #and add 1 to "wrongs".
                    if tries == 3 and (solved + wrongs) < maximum_points:
                        print(f"{x} + {y} =", str(x+y))
                        x = generate_integer(a)
                        y = generate_integer(a)
                        wrongs += 1
                        tries = 0
                    #If tries equal 3 and the sum of solved and wrongs are equal to the
                    #total of problems, print the score and break the loop.
                    elif tries == 3 and (solved + wrongs) == maximum_points:
                        print(f"Score: {int(10*solved/maximum_points)}")
                        print(f"Score of solved: {int(solved)}")
                        break
                    #Else, print "EEE".
                    else:
                        print("EEE")
                #If input isn't a digit, print "EEE" and add 1 to tries.
                else:
                    print("EEE")
                    tries += 1
        #If user already inputed 3 tries and hasn't solved all the problems,
        #print the correct answer, generate new numbers, resent the tries and
        #add 1 to "wrongs".
        elif tries == 3 and (solved + wrongs) < maximum_points:
            #print("EEE")
            print(f"{x} + {y} =", str(x+y))
            x = generate_integer(a)
            y = generate_integer(a)
            wrongs += 1
            tries = 0
        #If tries equal to 3 and user has solved all the problems, print the total
        #final score and break the loop.
        elif tries == 3 and (solved + wrongs) == maximum_points:
            #print(f"Score: {int(10*solved/maximum_points)}")
            print(f"Score of solved: {int(solved)}")
            print(f"Wrongs: {int(wrongs)}")
            break
        #else
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



