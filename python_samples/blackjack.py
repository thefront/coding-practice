#!/usr/bin/env python
''' A simplified version of Blackjack. No aces and no dealer yet. '''

import random

repeat = "y"
card1 = random.randint(1,10)
card2 = random.randint(1,10)
dealer1 = random.randint(1,10)

print "Let's play Blackjack!"

while repeat != "n":
    print "Your hand is %s and %s" % (card1, card2)
    total = card1 + card2
    hit = "y"

    while hit != "n":
        print "A total of %s" % total
        anotherCard = raw_input('Do you want another card? [y/n]: ')

        if anotherCard == "y":
            newcard = random.randint(1,10)
            total += newcard
            print "You new card is %s" % newcard

            if total > 21:
                print "Bust! you went over 21!"
                hit ="n"
            if total == 21:
                print "You Win!, you hit 21!"
                hit = "n"
        elif anotherCard == "n":
            hit = "n"
        else:
            print "I don't recognize your response"

    repeat = raw_input("Do you want to play again?")
    if repeat == "n":
        print "Goodbye!"
    elif repeat == "y":
        print "Right on! My kind of gambler!"
    else:
        print "I didn't recognize the input, Goodbye!"
        repeat = "n"
#EOF
