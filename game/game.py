
import random

guesses = 0

while True:
    try:
        top_of_range = input("Level: ")
        print(top_of_range)
        if top_of_range.isdigit() and int(top_of_range) > 0:
            top_of_range = int(top_of_range)
            random_number = random.randint(0, top_of_range)
            guesses += 1
            guess = int(input("Guess: "))
            if guess < random_number:
                print("Too small!")
            elif guess > random_number:
                print("Too large!")
            else:
                print("Just right!")
                break
        else:
            continue
    except:
        break


