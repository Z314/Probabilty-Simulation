import random

# The Dice class for the dice simulation
# Used in dice_main.py
# Also demonstrates calling the __str__ method in Dice class
# Author: JP
# Tested with version: 3.6

class Dice:
    """
    Dice class simulates dice  getting rolled
    """

    def __init__(self):
        """
        __init__method initialises the sideup data attribute with heads
        Attribute is set private with double underscore before name
        this means that only the objects methods can access the attribute...
        i.e., can't be directly accessed by statements not in the Coin class methods.
        Protects from corruption etc.
        """
        self.__sideup = 'one' # attribute set as private


    def toss(self):
        """
        Tosses the dice and returns the side up.
        myRandom: int, dice side face up
        self.__sideup: string, attribute of class that stores the result
        """
        myRandom = random.randint(1, 6)
        print("this is myRandom: ",  myRandom)
        if myRandom == 1:
            self.__sideup = 'one'
        elif myRandom == 2: 
            self.__sideup = 'two'
        elif myRandom == 3: 
            self.__sideup = 'three'
        elif myRandom == 4: 
            self.__sideup = 'four'
        elif myRandom == 5: 
            self.__sideup = 'five'
        elif myRandom == 6: 
            self.__sideup = 'six'

            
        

    def get_sideUp(self):
        """
        Retrieves the face side up value (string)
        """
        return self.__sideup

    def __str__(self):
        """
        Optional method for illustration.
        This is an optional special method. It returns a string, showing the attribute values when called by the print statement.
        You don't call this method. It is auto called when you call the 'print (name of object)' or pythons internal 'str(name of object)'
        """
        return self.__sideup