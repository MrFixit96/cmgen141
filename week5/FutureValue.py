#
#     Program: FutureValue
#     File: FutureValue.py
#     Author: James Anderton
#     Date: 25-SEP-2017
#     Purpose: A program that prompts the user to enter the account's present value, monthly interest
#               rate, and the number of months that the money will be left in the account and will
#               display the account's future value.
#

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
                    print("Exiting...")
                    exit()
                elif menuChoice == "Y":
                    term, interest, presentVal = getUserInput()
                    newAmount = calculate(term, interest, presentVal)
                    displayVal(term, interest,presentVal,newAmount)
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
#   RETURNS: term, interest, presentVal
#
#########################################################
def getUserInput():
    while True:
        try:
            term = int(input("\tPlease enter the number of months to calculate interest for: "))
            interest = float(input("\tPlease enter the amount of interest being charged: "))
            presentVal = float(input("\tPlease enter the starting amount of the account: "))
        except ValueError:
            print("Please enter a valid number")
        else:
            break
    return term, interest, presentVal
# EndSub



#########################################################
#
#   SUB: calculate
#   REQUIRES: term, interest, presentVal
#   RETURNS: futureVal
#
#########################################################
def calculate(term, interest, presentVal):
    temp =(1+ (interest/100))**term
    futureVal = temp * presentVal

    return futureVal
# EndSub

#########################################################
#
#   SUB: displayVal
#   REQUIRES: term, interest, presentVal, futureVal
#
#########################################################
def displayVal(term, interest, presentVal, futureVal):

    print("Starting Amt. $ \tTerm\tInterest\tFuture Amt. $")
    print("================================================")
    print("$" + str(presentVal), "\t\t\t\t", term, "\t", "%" + str(interest), "\t\t", "$" + str(format(futureVal, ',.2f')))

# EndSUB

#########################################################
#
#                       MAIN
#
#########################################################

# Start Main Program
showMenu()
