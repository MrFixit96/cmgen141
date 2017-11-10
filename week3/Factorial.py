'''
    Program: Factorial
    File: Factorial.py
    Author: James Anderton
    Date: 14-SEP-2017
    Purpose: A simple menu program
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
                print("Factorial Calculator")
                print("==================================")
                print("\t1. Start Program")
                print("\t0. Exit")
                print()

                # get the next choice
                menuChoice = int(input("Select option: "))
                try:
                    if menuChoice == 1:
                        process(int(input("Enter the non-negative number to calculate a factorial for: ")))
                    elif menuChoice == 0:
                        exit()

                    # EndIf
                except ValueError:
                    print("Please enter a valid number")

                # EndTry
                showMenu()

            # EndWhile
            break

            # EndWhile
        except ValueError:
            print("Please type in a valid number. \n")

        # EndTry
    # EndWhile
# EndSub

#########################################################
#
#   SUB: Process
#
#########################################################
def process(num):
    # Validate input
    if num < 0:
        print("Please enter a non-negative number")
        showMenu()
    # EndIf

    # Setup the printout of the factorial
    printNum = num + 1
    print(str(num) + "! = ",end="")
    for i in range(printNum):
        if i == 0:
            continue

        # EndIF
        if i == int(num):
            print(i,end=" ")
        else:
            print(i,"x ", end="")

        # EndIf
    # EndFor
    print("=", end=" ")

    # Do the Actual Calculating
    num1 = 1
    for i in range(num + 1):
        if i == 0:
            continue

        # EndIF
        num1 = num1 * i

    # EndFor
    # Show the Answer
    print(num1)
    print()

# EndSub

#########################################################
#
#                   MAIN
#
#########################################################

showMenu()
