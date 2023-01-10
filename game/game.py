
import random

guesses = 0

while True:
    top_of_range = input("Level: ")
    if top_of_range.isdigit() and int(top_of_range) > 0:
        random_number = random.randint(0, top_of_range)
        guesses += 1
        guess = input("Guess: ")
        i



    else:
        print('Por favor intenta escribiendo un número.')
        continue

    guesses += 1
    user_guess = input(f"Adivina un número entre 0 y {top_of_range}: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Por favor escribe un número la próxima vez.')
        continue
    if user_guess == random_number:
        print("Adivinaste!")
        break
    else:
        if user_guess > random_number:
            print('Estuviste por encima del número, intentalo de nuevo!')
        elif user_guess < random_number:
            print("Estuviste por debajo de número, intentalo de nuevo!")

print("Lo adivinaste en " + str(guesses) + " intentos.")
