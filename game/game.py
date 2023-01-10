
import random

guesses = 0
top_of_range = input("Level: ")

while True:

    try:
        if top_of_range.isdigit() and int(top_of_range) > 0:
            top_of_range = int(top_of_range)
            random_number = random.randint(0, top_of_range)
            guesses += 1
            guess = int(input("Guess: "))
            if guess < random_number:
                print("Too small!")
                continue
            elif guess > random_number:
                print("Too large!")
                continue
            else:
                print("Just right!")
                break
        else:
            continue
    except:
        print("Hubo un error!)
        continue


10