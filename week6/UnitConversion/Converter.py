#
#     Program: Converter
#     File: Converter.py
#     Author: James Anderton
#     Date: 03-OCT-2017
#     Purpose: a program that allows a user to choose mass or length conversion,
#               enter a conversion amount, pick a current scale and convert to another scale...
#               program should allow standard-to-standard, standard-to-metric, metric-to-metric,
#               and metric to standard conversions.
#    Requires: Length.py and Mass.py
#

from week6.UnitConversion import Mass
from week6.UnitConversion import Length


def displayMenu():
    menuChoice = -99  # Used to get loop started
    while menuChoice < 0 or menuChoice > 3:
        # Show the Menu
        print("Physics Calculations Menu")
        print("==================================")
        print("\t1. Convert the length to a different unit")
        print("\t2. Convert a mass of an object to a different unit")
        print("\t0. Exit")
        print()

        # get the next choice
        menuChoice = int(input("Select option: "))

        if menuChoice == 1:
            unitIn, unitOut, lengthIn = Length.getInput()
            lengthOut = Length.chooseScale(unitIn, unitOut, lengthIn)
            Length.displayResults(lengthIn, lengthOut, unitIn, unitOut)
        elif menuChoice == 2:
            mass, velocity = Mass.getInput()
            energy = Mass.kineticEnergy(mass, velocity)
            Mass.displayResults(mass, velocity, energy)

        elif menuChoice == 0:
            print("Exiting...")
            exit(0)
        else:
            print("Please enter a valid menu choice. \n")
            continue

#########################################################
#
#   SUB: Main
#
#########################################################
def Main():


    while True:
        try:

            displayMenu()
            # EndWhile

        except ValueError:
            print("Please choose a valid menu option. \n")
        # EndTry
    # EndWhile
# EndSub

#########################################################
#
#                       RUNNER
#
#########################################################

Main()
