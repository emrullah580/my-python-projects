import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess_numbers = int(input("Please enter an integer: "))
        attempts += 1

        if guess_numbers > number:
            print("Too high!")
            
        elif guess_numbers < number:
            print("Too low!")
            
        elif guess_numbers==number:
            print("Correct!")
            print("Congrats!")
            break 
        
        if attempts >= 3:
            break
        
        
guess_the_number()