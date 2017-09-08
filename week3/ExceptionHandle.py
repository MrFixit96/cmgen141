'''
    Program: ExceptionHandle
    File: ExceptionHandle.py
    Author: James Anderton
    Date: 7-SEP-2017
    Purpose: A simple menu program
'''


def showMenu():
    menuChoice = -99  # Used to get loop started

    while True:
        try:
            while menuChoice < 0 or menuChoice > 3:
                # Show the Menu
                print("Employee Records Menu")
                print("==================================")
                print("\t1. Search for employee")
                print("\t2. Add employee")
                print("\t3. Delete employee")
                print("\t0. Exit")
                print()

                # get the next choice
                menuChoice = int(input("Select option: "))

            break

        except ValueError:
            print("Please type in a valid number. \n")

showMenu()