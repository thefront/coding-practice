#!/usr/bin/env python
# this is a practice program from java class
# writing this in python for practice
# description: prompt user for number of astericks to print out, print them,
#              then ask user to repeat or not
#
# inputs: number and where to repeat or not
# outputs: number of astericks

# assign variable whether to repeat to yes
goAgain = "y"

# start loop
while goAgain != "n":

    # prompt for astericks
    print "How many astericks do you want to print? ",
    numAstericks = raw_input()
    # other way
    # numAstericks = rawinput("How many astericks do you want to print? ")

    # iterate through to print astericks
    #for i in range (0, int(numAstericks)):
    #    print "*"
    print(int(numAstericks) * "*")

    # ask to go again?
    goAgain = raw_input("Do you want to go again? [y/n]: ")
# EOF
