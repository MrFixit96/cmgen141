'''
    Program: DistanceTraveled
    File: DistanceTraveled.py
    Author: James Anderton
    Date: 13-SEP-2017
    Purpose: A program that asks the user for the speed of a vehicle (in miles per hour)
            and the number of hours it has traveled. It should then use a loop to display the distance
            the vehicle has traveled for each hour of that time period.
'''

#########################################################
#
#   SUB: showMenu
#
#########################################################
def showMenu():
    # Get loop started
    print("Distance Traveled Calculator")
    print("==================================")
    menuChoice = (input('Start Program? "Y/N" ')).capitalize()

    while True:
        try:
            while menuChoice !=0:
                if menuChoice == "N":
                    exit()
                elif menuChoice == "Y":
                    speed, time = getUserInput()
                    displayDist(speed, time)
                else:
                    print("Please type in a valid choice. \n")

                # EndIf
                #Get Next Choice
                menuChoice = (input('Start Program? "Y/N" ')).capitalize()

            # EndWhile
            break

        except ValueError:
            print("Please type in a valid choice. \n")

        # EndTry
    # EndWhile
# EndSub

#########################################################
#
#   SUB: getUserInput
#   RETURNS: speed, time
#
#########################################################
def getUserInput():
    speed = input("\tPlease enter the rate of speed: ")
    time = input("\tPlease enter the length time traveled: ")
    return speed, time
# EndSub

#########################################################
#
#   SUB: displayDist
#   REQUIRES: speed, time
#
#########################################################
def displayDist(speed, time):
    speed = int(speed)
    time = float(time)
    print("Hour\t\tDistance Traveled")
    print("===========================")

    i = time
    c = 0

    while i > 0 and i <= time:
        if i >= 1:
            c += 1
        else:
            c += i

        # EndIf
        print(c, "\t\t\t", speed * c)
        i -= 1

    # EndWhile
# EndSUB

#########################################################
#
#                       MAIN
#
#########################################################

# Start Main Program
showMenu()
