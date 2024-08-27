import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess_numbers = int(input("PLease enter an integer"))
        attempts += 1
        
guess_the_number()