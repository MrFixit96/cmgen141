'''
    Program: PennyPay
    File: PennyPay.py
    Author: James Anderton
    Date: 13-Sept-2017
    Purpose: a program that calculates the amount of money a person would earn over a period
            of time if his or her salary is one coin the first day, two coins the second day, and
            continues to double each day.
'''

#########################################################
#
#   SUB: showMenu
#
#########################################################
def showMenu():
    menuChoice = -99  # Used to get loop started

    while True:
        try:
            while menuChoice < 0 or menuChoice > 1:
                # Show the Menu
                print("Penny Pay Program Menu")
                print("==================================")
                print("\t1. Start the program")
                print("\t0. Exit")
                print()

                # get the next choice
                menuChoice = int(input("Select option: "))
                try:
                    if menuChoice == 1:
                        pay(int(input("Enter the number of days to calculate ")))
                    elif menuChoice == 0:
                        exit()

                    # EndIf
                except ValueError:
                    print("Please enter a valid number of days")

                # EndTry
                showMenu()

            # EndWhile
            break

        except ValueError:
            print("Please type in a valid menu choice. \n")

        # EndTry
# EndSub

#########################################################
#
#   SUB: pay
#   Requires: limit
#
#########################################################
def pay(limit):
    cType = input("Are the coins being earned Penny, Nickle, Dime, or Quarter? ")
    cVal = 0

    if cType == "Penny":
        cVal = 1
    elif cType == "Nickle":
        cVal = 5
    elif cType == "Dime":
        cVal = 10
    elif cType == "Quarter":
        cVal = 25
    else:
        print("Please enter a valid choice")
        pay(limit)

    # EndIf
    num1 = 1
    num2 = 1
    print("=============== " + cType + " Pay ===================")
    print("Day#\t\tTotal Earned")
    print("1\t\t\t " + str(num1))

    for i in range(int(limit)):
        num2 = num1 * 2
        num1 = num2
        amount = float((num2 * cVal) / 100)
        print(i, "\t\t\t$", format(amount, ".2f"))

    # EndFor
    print()

# Go back to main Menu
showMenu()
# EndSub

#########################################################
#
#                       MAIN
#
#########################################################

showMenu()
