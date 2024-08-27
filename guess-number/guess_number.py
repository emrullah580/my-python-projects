import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5 

    print("Welcome to the number guessing game!")
    print("I've chosen a number between 1 and 100. Can you guess it?")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == number:
            print(f"Congratulations! You guessed the number ({number}) in {attempts} attempts.")
            return
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

    print(f"Sorry, you ran out of attempts. The number was {number}.")

guess_the_number()