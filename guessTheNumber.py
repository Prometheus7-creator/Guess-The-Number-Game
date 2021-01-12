# Guess the number

import random

MAX_GUESSES = 5  # maximum number of guesses allowed
MAX_RANGE = 20   # highest possible number

# show introduction
print('Welcome to my guess the number program.')
print('Guess my number between 1 and', MAX_RANGE)
print('You will have', MAX_GUESSES, 'guesses.')

def playOneRound():

    # choose random target
    target = random.randrange(1, MAX_RANGE + 1)

    # initialize a guess counter
    guessCounter = 0

    # loop forever
    while True:
        # ask the user for a guess
        
        userGuess = input('Take a guess: ')

        # check for potential error
        try:
            userGuess = int(userGuess)
        except:
            print ('Hey, that was NOT an integer!')
            continue  #transfer control back to the while

        # increament guess counter
        guessCounter = guessCounter +1

        # if the user is correct, congratulate user, we're done

        if userGuess == target:
            print('You got it!')
            print('It only took you', guessCounter, 'guess(es).')
            break
        # if user's guess is too low, tell user

        elif userGuess < target:
            print('Your guess was too low.')

        # if user's guess is too high, tell user
        else:
            print('Your guess was too high ')

        # if reached max guesses, tell answer correct answer, we're done.
        if guessCounter == 5:
            print('Sorry, you did not get it in 5 guesses')
            print('The number was:', target)
            break

# main code
while True:
    
    playOneRound()  # call a function to play one round of the game
    goAgain = input('Play again? (Press ENTER to continue, or q to quit): ')

    if goAgain == 'q':
        break
        
print('Thanks for playing.')
