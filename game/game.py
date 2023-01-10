
import random

def main():
    while True:
        top_of_range = input("Level: ")
        if top_of_range.isdigit() and int(top_of_range) > 0:
            top_of_range = int(top_of_range)
            random_number = random.randint(0, top_of_range)
            break
        print("Try with a number")
        break
        #continue

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < random_number:
                print("Too small!")

            elif guess > random_number:
                print("Too large!")
            else:
                print("Just right!")
                break
        except:
            print("Hubo un error!")
            break
        else:
            continue

main()