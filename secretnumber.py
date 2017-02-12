
#-*- coding: utf-8 -*-
import random

# GUESS THE SECRET NUMBER v2

def setsecretnumberbetween(a,b):
    result = random.randint(a,b)
    return result

def main():
    print("###################################################")
    print("## Welcome to 'The Finding Of The Secret Number' ##")
    print("###################################################\n")
    maxtries = None
    while maxtries is None:
        try:
            maxtries = int(raw_input("Enter a number of max try's: "))
        except ValueError:
            print("You didn't enter an integer number, please try again.")

    inputa = None
    while inputa is None:
        try:
            inputa = int(raw_input("The secret number should be in the range FROM: "))
        except ValueError:
            print("You didn't enter an integer number, please try again.")

    inputb = None
    while inputb is None:
        try:
            inputb = int(raw_input("The secret number should be in the range TO: "))
        except ValueError:
            print("You didn't enter an integer number, please try again.")

    guess = None
    currenttry = 1

    secret = setsecretnumberbetween(inputa, inputb)

    while guess != secret and currenttry <= maxtries:
        print("This is try " + str(currenttry) + " of a total of " + str(maxtries) + " tries.")
        guess = int(raw_input("Enter your guess of the secret number: "))
        if guess != secret:
            currenttry += 1  # selber wie 'currentry = currenttry + 1'
            print("Sorry you missed! That was a wrong guess.\n")
        else:
            print("STRIKE! You found the the secret number '%i'.\n" % secret)
            print("################")
            print("## Game Over. ##")
            print("################")

    if guess != secret:
        print("You've reached the max tries limit of %i.\n" % maxtries)
        print("################")
        print("## Game Over. ##")
        print("################")


if __name__ == '__main__':
    main()