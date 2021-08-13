import random



def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    guess = 0
    while feedback != 'c':
        try:
            if high!=low: guess = random.randint(low,high)
            else: guess = low # or guess = high
        
            feedback = input(f'Is {guess} too high (H), too low(L), or correct(C)? ').lower()

            if feedback == 'h': high = guess -1
            elif feedback == 'l': low = guess +1
            elif feedback!= 'c': print("I don't understand")


        except:
            print('Please dont cheat! LETS PLAY AGAIN!!!')
            low = 1
            high = x
            continue
        
    print(f'Congrats!!! The computer guessed your number {guess} correctly!.')

computer_guess(10)
