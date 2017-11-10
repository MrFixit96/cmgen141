'''
    Program: Week4_DistanceTraveled
    File: Week4_DistanceTraveled.py
    Author: James Anderton
    Date: 20-SEP-2017
    Purpose: A program that asks the user for the speed of a vehicle (in miles per hour)
            and the number of hours it has traveled. It should then use a loop to display the distance
            the vehicle has traveled for each hour of that time period. Limit the time driven to 24 hours
            and the speed to 1 - 100. Make sure the program can be ran repeatedly until the user decides to quit
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
    while True:
        try:
            speed = int(input("\tPlease enter the rate of speed up to 100mph: "))
            if speed <= 100:
                break
        except ValueError:
            print("Please enter a valid number between 0 - 100")

    while True:
        try:
            time = float(input("\tPlease enter the length time traveled up to 24hrs: "))
            if time <= 24:
                break
        except ValueError:
            print("Please enter a valid number between 0 and 24")

    return speed, time
# EndSub

#########################################################
#
#   SUB: displayDist
#   REQUIRES: speed, time
#
#########################################################
def displayDist(speed, time):

    print("Hour\t\tDistance Traveled")
    print("===========================")

    index = time
    count = 0

    while index > 0 and index <= time:
        if index >= 1:
            count += 1
        else:
            count += index

        # EndIf
        print(count, "\t\t\t", speed * count)
        index -= 1

    # EndWhile
# EndSUB

#########################################################
#
#                       MAIN
#
#########################################################

# Start Main Program
showMenu()
