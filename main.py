from colorama import Fore, Style

import random as rd
name = input("Whats your name bro : ")
number = rd.randint(1,100)
print(f"\nAlright {name}, I'm thinking of a number between 1 and 100.")
print("Can you guess what it is?")



def check(guess):
    if guess > number:
        print(Fore.RED + f"Ahh too high, {name}!" + Style.RESET_ALL)
    elif guess < number:
        print(Fore.RED + f"Ohh too low,  {name}!" + Style.RESET_ALL)
    else:
         print(f'Yoo u nailed it {name}')
    
    
attempt = 0          
while attempt < 10:
    attempt += 1
    try:
        user_input = int(input(f"Guess a number {name}: "))
        if user_input > 100 or user_input < 1:
            raise ValueError    
    except ValueError:
            print(f"Hey, {name} enter a valid number from 1 to 100")
            continue

    check(user_input)

    print(f"Attempts left: {10 - attempt}")


    if user_input == number:
         print(Fore.GREEN + f"Yoo {name}, you nailed it in {attempt} tries!" + Style.RESET_ALL)
         break
    
else:
        print(f"Yoo {name}, you are out of attempts.")
        print(Fore.RED + "Game Over" + Style.RESET_ALL)

    

    
    
    


    
        