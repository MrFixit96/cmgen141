"""
    Program: NAME OF PROGRAM
    File: sample.py
    Author: James Anderton
    Date: 24-Aug-2017
    Purpose: SOME REASON TO EXIST
"""

#########################################################
#
#   SUB: showMenu
#
#########################################################
def showMenu():
    menuChoice = -99  # Used to get loop started

    while True:
        try:
            while menuChoice < 0 or menuChoice > 3:
                # Show the Menu
                print("Sample Menu")
                print("==================================")
                print("\t1. Sample 1")
                print("\t2. Sample 2")
                print("\t3. Sample 3")
                print("\t0. Exit")
                print()

                # get the next choice
                menuChoice = int(input("Select option: "))

            # EndWhile
            break

        except ValueError:
            print("Please type in a valid number. \n")
        # EndTry
    # EndWhile
# EndSub

#########################################################
#
#                       MAIN
#
#########################################################

showMenu()


# SAMPLES
#*****************************************************************************************************

variableNAME = "stuff"
CONSTANT = 'stuff'


class Elephant:
    def __init__(self):
        pass

    def method(self):
        pass


myElephant = Elephant()
