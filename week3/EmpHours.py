'''
    Program: EmpHours
    File: EmpHours.py
    Author: James Anderton
    Date: 7-SEP-2017
    Purpose: A program to total the departments total hours for the week
'''


def totalEmpHours():
    # INITIALIZE
    totalEmpHours = 0
    empNum = input("Enter employee # to continue or 0000 to quit: ")

    # TEST
    while empNum != "0000":

        # PROCESS
        empHours = float(input("Enter employee hours: "))
        totalEmpHours += empHours

        # INCREMENT
        empNum = input("Enter employee # to continue or 0000 to quit: ")

    print("Total department hours ==> ", totalEmpHours)


totalEmpHours()