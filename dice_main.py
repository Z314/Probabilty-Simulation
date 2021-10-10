# The main function for the dice simulation
# Imports module we named dice.py (has the Dice class definition)
# Also demonstrates calling the __str__ method in Dice class
# Change Number_of_DiceRolls to any integer value, to simulate dice rolls.
# Author: JP
# Tested with version: 3.6

import numpy as np
import dice
import matplotlib.pyplot as plt
import scipy as sp

def main():

    # create object (instance of class) from Dice class
    a_dice1 = dice.Dice() # object = filename where class located . class name
    faceNumber = {"one":0, "two":0, "three":0, "four":0, "five":0, "six":0 }

    
    Number_of_DiceRolls = int(input("Enter a integer number greater than 0: ")) # change to what you like
    for i in range(Number_of_DiceRolls):

        print('The side up is: ', a_dice1.get_sideUp())

        print('Lets toss the dice... ')
        a_dice1.toss()

        
        side = a_dice1.get_sideUp()
        print('This is the side now facing up: ', side)

        # stores the number of times each face value came up
        if side=="one":
            faceNumber["one"] = faceNumber["one"] + 1
        elif side=="two":
            faceNumber["two"] = faceNumber["two"] + 1
        elif side=="three":
            faceNumber["three"] = faceNumber["two"] + 1
        elif side=="four":
            faceNumber["four"] = faceNumber["two"] + 1
        elif side=="five":
            faceNumber["five"] = faceNumber["two"] + 1
        elif side=="six":
            faceNumber["six"] = faceNumber["two"] + 1

        # just shows the use of the __str__ method in Dice class
        # calling the __str__ method (called automatically). Shows the attribute values
        print(a_dice1)
        # or can call this way:
        print(str(a_dice1))
        
    
    # plot the results
    names = list(faceNumber.keys())
    values = list(faceNumber.values())

    plt.bar(range(len(faceNumber)), values, tick_label=names)
    plt.title("Dice Rolling Simulation")
    plt.xlabel("Dice face value")
    plt.ylabel("Number of times face value has shown")
    plt.show()
      
# call main function
main()
