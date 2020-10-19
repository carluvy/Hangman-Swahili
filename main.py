import time
from random_words import RandomWords


def hangman():
    # welcome the user
    name = input('What is your name?')
    print('Hi,' + name, "It's time to play Hangman in Swahili!")
    print('')

    # wait for 1 second
    time.sleep(1)

    print('Start guessing letters...')
    time.sleep(0.5)

    words = RandomWords()
    word = words.random_word()

    # create a variable with an empty value
    guesses = ''

    # determine the number of turns
    turns = 6

    # create a while loop
    # check if the turns are more than zero
    while turns > 0:
        # make counter that starts with zero
        failed = 0

        # for every character in random word
        for char in word:
            # see if character is in the player's guess
            if char in guesses:
                # print the character
                print(char)
            else:
                # if not found, print a dash
                print('_')
                # and increase the failed counter with one
                failed += 1
        #  if failed is zero
        # print you won
        if failed == 0:
            print('You Won!')
            # exit the script
            break
        # ask th user to guess a character
        guess = input('guess a letter:')

        # set the player's guess to guesses
        guesses += guess

        # if the guess is not found in the word
        if guess not in word:
            # turns counter decreases with 1 (5 now)
            turns -= 1
            print('Wrong')

            # how many turns are lefy
            print('You have', + turns, 'more guesses')
            # if the turns are equal to zero
            if turns == 0:
                # print you lose
                print('You Lose')
                print(word)


hangman()
