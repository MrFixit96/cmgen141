#
#     Program: Physics
#     File: Converter.py
#     Author: James Anderton
#     Date: 03-OCT-2017
#     Purpose: a program that allows the user to choose between calculating the falling distance of an object
#               or calculates an objects kinetic energy.
#    Requires: Length.py and Mass.py
#

from week6.Physics import KineticEnergy
from week6.Physics import FallingDistance


def displayMenu():
    menuChoice = -99  # Used to get loop started
    while menuChoice < 0 or menuChoice > 3:
        # Show the Menu
        print("Physics Calculations Menu")
        print("==================================")
        print("\t1. Calculate the falling distance of an object")
        print("\t2. Calculate an object's kinetic energy")
        print("\t0. Exit")
        print()

        # get the next choice
        menuChoice = int(input("Select option: "))

        if menuChoice == 1:
            fallingSecs = FallingDistance.getInput()
            distance = FallingDistance.fallingDistance(fallingSecs)
            FallingDistance.displayResults(distance, fallingSecs)

        elif menuChoice == 2:
            mass, velocity = KineticEnergy.getInput()
            energy = KineticEnergy.kineticEnergy(mass, velocity)
            KineticEnergy.displayResults(mass, velocity, energy)

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
