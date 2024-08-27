import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess_numbers = int(input("Lütfen Bir Değer Giriniz: "))
        attempts += 1
        if attempts>3:
            break
        
        elif guess_numbers>number:
            print("Daha küçük değer gir ")
            
        elif guess_numbers<number:
            print("Daha büyük değer gir ")
            
        elif guess_numbers==number:
            print("D O Ğ R U")
            print("Tebrikler")
            break 
        
     
        
guess_the_number()