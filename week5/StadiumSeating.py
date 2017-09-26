#
#     Program: StadiumSeating
#     File: StadiumSeating.py
#     Author: James Anderton
#     Date: 24-SEP-2017
#     Purpose: A program that asks how many tickets for each class
#               of seats were sold, then displays the amount of income generated from ticket sales.
#               -Class A seats cost $20
#               -Class B seats cost $15
#               -Class C seats cost $10.
#


#########################################################
#
#   SUB: getInput
#
#########################################################
def getInput():
    clsA = int(input("How many Class A seats were sold? "))
    clsB = int(input("How many Class A seats were sold? "))
    clsC = int(input("How many Class A seats were sold? "))

    return clsA, clsB, clsC
# EndSub


#########################################################
#
#   SUB: calculateInc
#
#########################################################
def calculateInc(clsA, clsB, clsC):
    clsACost = clsA * 20
    clsBCost = clsB * 15
    clsCCost = clsC * 10
    totalInc = clsACost + clsBCost + clsCCost

    return totalInc
# EndSub


#########################################################
#
#   SUB: displayInc
#
#########################################################
def displayInc(clsA, clsB, clsC, totalInc):
    print("==================================")
    print("Ticket Totals")
    print("==================================")
    print()

    print("There were", clsA, "Class A tickets sold.")
    print("There were", clsB, "Class B tickets sold.")
    print("There were", clsC, "Class C tickets sold.")
    print("==================================")
    print()
    print("For a total of $", format(totalInc, ',.2f'), "in ticket sales.")

# EndSub


#########################################################
#
#   SUB: Main
#
#########################################################
def main():
    menuChoice = input("Press Y to Start or N to Exit").upper()  # Used to get loop started

    while True:
        try:
            while menuChoice == "Y" or menuChoice == "N":
                if menuChoice != "N":
                    # Show the MenuY
                    print()
                    print("Stadium Seating")
                    print("==================================")
                    print()

                    # get the next choice

                    clsA, clsB, clsC = getInput()
                    totalInc = calculateInc(clsA, clsB, clsC)
                    displayInc(clsA, clsB, clsC, totalInc)

                    menuChoice = input("Press Y to Start or N to Exit").upper()
                elif menuChoice == "N":
                    print("Exiting Program...")
                    exit(0)
                else:
                    print("Please type in a valid choice. \n")
                    menuChoice = input("Press Y to Start or N to Exit").upper()

            # EndWhile
            break
        except ValueError:
            print("Please type in a valid choice. \n")
        # EndTry
    # EndWhile
    print("Please type in a valid choice. \n")
    main()
# EndSub

#########################################################
#
#                       MAIN
#
#########################################################

main()
