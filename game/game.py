
#Score: 9/8

import random

def main():
    while True:
        top_of_range = input("Level: ")
        if top_of_range.isdigit() and int(top_of_range) > 0:
            top_of_range = int(top_of_range)
            random_number = random.randint(1, top_of_range)
            break
        else:
            #print("Try with a number")
            continue
        #continue

    while True:
        try:
            guess = int(input("Guess: "))
            if 1 <= guess <= top_of_range:
                if guess == random_number:
                    print("Just right!")
                    break
                elif guess < random_number:
                    print("Too small!")
                elif guess > random_number:
                    print("Too large!")
        except:
            continue

main()