#!/usr/bin/env python
# number guessing program

def main():
    playOneGame()

    while shouldPlayAgain():
        playOneGame()
# end of main


def shouldPlayAgain():

    answer = raw_input("Great! Do you want to play again? [y/n]: ").lower()

    if answer == 'y':
        return True;
    elif answer == 'n':
        return False
    else:
        print "I didn't understand your response. Exiting."
        return False
# end of shouldPlayAgain


def playOneGame():
    low = 0
    high = 100
    middle = 50
    loop = True

    print "Guess a number between 1 and 100."

    while loop:
        guessAgain = getUserResponseToGuess(middle)

        if guessAgain == 'l':
            high = middle
            middle = getMidPoint(low, high)
        elif guessAgain == 'h':
            low = middle
            middle = getMidPoint(low, high)
        elif guessAgain == 'c':
            loop = False
        else:
            print "I didn't understand your response."
# end of playOneGame


def getMidPoint(low, high):
    return (low + high)/2
# end of getMidPoint


def getUserResponseToGuess(middleNum):
    return raw_input("Is it %s? (h/l/c): " % middleNum).lower()
# end of getUserResponseToGuess


if __name__ == '__main__':
    main()
# EOF
