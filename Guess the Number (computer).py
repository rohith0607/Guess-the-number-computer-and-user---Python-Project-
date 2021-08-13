import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess!=random_number:
        try:
            guess = int(input(f'Guess a number between 1 and {x}: '))
        except:
            print(f"Sorry! I don't understand what are you saying. Enter a natural number between 1 and {x}\n")
            continue
        if guess < random_number: print('Sorry, guess again. Too low.')
        elif guess > random_number: print('Sorry, guess again. Too high.')
        else: print(f'Congrats. You have guessed the number {random_number} correctly')
        print('\n')

guess(10)
