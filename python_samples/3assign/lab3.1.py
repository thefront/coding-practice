#!/usr/local/bin/python3
# NAME: Richard Tzeng
# FILE: lab3.1.py
# DATE: <21014-07-11 Fri>
# DESC: This function rps_game_winner takes a two element list and tests who
# wins in Rock, Paper, Sissors. It test for number of players and if one of the
# elements is not R, P, or S (case-insensitive). 

class WrongNumberOfPlayersError(Exception): pass
class NoSuchStrategyError(Exception): pass

def __main__():
    """ __main__() is for testing the code. This will be executed
    when you run the module as a standalone program.
    """

    #Test cases
    good_game = [["Armando", "P"], ["Dave", "S"]]
    bad_strategy = [["Armando", "p"], ["Dave", "g"]]
    not_enough = ["Armando", "P"]
    print("The winner is ", end='')

    # A known good match
    try:
        print(rps_game_winner(good_game))
    except:
        print("This test should not fail")

    # Not enough players
    try:
        print(rps_game_winner(not_enough))
    except:
        print("This test was for not enough players: ", end="")
        print(not_enough)

    # One of the choices wasn't correct, RPS
    try:
        print(rps_game_winner(bad_strategy))
    except:
        print("This test was for someone not using RPS: ", end="")
        print(bad_strategy)


def rps_game_winner(game):
    """ This function returns the winner of RPS.  It also test for right
    number of players and if they used the right selction of RPS.
    Rules of Rock-Paper-Scissors

    Games must have two players
    Valid strategies are: R, P, and S
    R beats S
    S beats P
    P beats R
    A tie goes to the first player

    Valid input: a list of 2 lists: [['Name1, 'Strategy'], ['Name2', 'Strategy]]
    where strategy is either R, P, or S
    """

    # separate the game into two lists, then set the 2nd elements to lcase
    playa1 = game[0]
    playa2 = game[1]
    play1_choice = playa1[1].lower()
    play2_choice = playa2[1].lower()

    # create a list to test correct strategy
    lcase = ['r', 'p', 's']
    
    # Test if there are 2 players
    if len(game) != 2:
        raise WrongNumberOfPlayersError('Wrong number of players!')

    # Test to see if strategy is R, P, or S
    elif play1_choice not in lcase or play2_choice not in lcase:
        raise NoSuchStrategyError('You have to choose R, P or S')

    # Determine winner by assigning choices to each player
    elif play1_choice == play2_choice:
        return  game[0]
    elif play1_choice == 'p' and play2_choice == 'r':
        return  game[0]
    elif play1_choice == 'p' and play2_choice == 's':
        return  game[1] 
    elif play1_choice == 'r' and play2_choice == 's':
        return  game[0]
    elif play1_choice == 'r' and play2_choice == 'p':
        return  game[1] 
    elif play1_choice == 's' and play2_choice == 'p':
        return  game[0] 
    elif play1_choice == 's' and play2_choice == 'r':
        return  game[1] 

# MAIN SECTION
if __name__ == '__main__':
    __main__()
