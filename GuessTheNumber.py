""" This app lets the user try to guess a randomly generated number"""
from random import randint

def title():
    """
        Function used to build the title of the app
    """
    print("--------------------------------------")
    print("       GUESS THE NUMBER APP")
    print("--------------------------------------")


def lets_play_a_game(low, high):
    """
        Initiates a game of Guess the Number
        :param low: the lowest value allowed for the user to guess
        :param high: the highest value allowed for the user to guess
    """
    ran = randint(low, high)
    inp = high+1
    title()

    while inp != ran:
        inp = int(input("Guess a number between {} and {}: ".format(low, high)))
        if inp == ran:
            print("Yes!! {} was the number. Congratulations!".format(inp))
        else:
            if inp > ran:
                print("Sorry but {} is Higher than the number".format(inp))
            else:
                print("Sorry but {} is Lower than the number".format(inp))


lets_play_a_game(1, 100)
