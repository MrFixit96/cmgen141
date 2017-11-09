#
#     Program: CreditCardValidator
#     File: CreditCardValidator.py
#     Author: James Anderton
#     Date: 26-OCT-2017
#     Purpose: A program to validate credit cards.
#           -check for card type (valid number shown below)
#           - 37 Amex - 371449635398431
#           -  4 Visa - 411111111111111
#           -  5 MC - 55555555554444
#           -  6 Discover - 6011111111111111111117
#       -must be from 13 to 16 digits long
#       -from right to left double all even numbered digits
#          - if doubling causes a two digit number subtract 9
#       -sum the even numbered digits after doubling
#       -sum the odd number digits
#       -add the even and odd sums
#       -if the total % 10 is 0 then the card is valid


#########################################################
#
#   SUB: Main
#
#########################################################
def Main():
    mnuChoice = 'Y'
    ccNum = -1
    sumEvens = -1
    sumOdds = -1
    isValid = False
    cardType = "None"

    while mnuChoice != 'Q':
        displayMenu()
        mnuChoice = setMenuChoice()
        if mnuChoice == 'N':
            ccNum = setNumber()
        elif mnuChoice == 'V' and ccNum != -1:

            sumEvens = setSumEvens(ccNum)

            sumOdds = setSumOdds(ccNum)

            total = sumOdds + sumEvens
            isValid = validateTotal(total)

            cardType = setCardType(ccNum)
            print("This card is a", cardType)
            displayResults(ccNum, isValid, cardType)
        elif mnuChoice == 'V':
            print('You have not entered a number - restart!')

    # EndWhile

# EndSub

#########################################################
#
#   SUB: displayMenu
#
#########################################################
def displayMenu():

    print('=== I Can\'t Count (ICC) Credit Card Validator ===')
    print('\t(N)umber entry:')
    print('\t(Validate number: ')
    print('\t(Q)uit program: ')
    print()
    print('\tEnter N, V, or Q:')


# EndSub

#########################################################
#
#       SUB: setMenuChoice
#
#########################################################
def setMenuChoice():
    choice = input()
    choice = choice[0].upper()

    while choice != 'N' and choice != 'V' and choice != 'Q':
        print("That is an invalid choice")
        displayMenu()
        choice = input()
        choice = choice[0].upper()

    # End While

    return choice
# EndSub


#########################################################
#
#       SUB: setNumber
#
#########################################################
def setNumber():
    num = input("Enter the CC Number: ")
    while not num.isdigit() or len(num) < 13 or len(num) > 16:
        print('Credit card number must be between 13 and 16 digits only')
        num = input('Re-enter the CC number: ')

    # EndWhile

    return num

# EndSub


#########################################################
#
#   Sub: setSumOdds
#
#########################################################
def setSumOdds(ccNum):
    sumOdds = 0
    wordLen = len(ccNum) -1

    for count in range(wordLen, -1, -2): #goes down to but not including -1
        num  = int(ccNum[count])
        print(num)

        sumOdds = sumOdds + num
    # EndFor

    return sumOdds

# EndSub


#########################################################
#
#   SUB: setSumEvens
#
#########################################################
def setSumEvens(ccNum):
    sumEven = 0
    wordLen = len(ccNum) -2

    for count in range(wordLen, -1, -2): #goes down to but not including -1
        num  = int(ccNum[count])*2
        print(num)

        if num > 9:
            num = num - 9
        # EndIF

        sumEven = sumEven + num
    # EndFor

    return sumEven

# EndSub


#########################################################
#
#   SUB: validateTotal
#
#########################################################
def validateTotal(total):
    isValid = False
    num = total % 10
    if num == 0:
        isValid = True
    # EndIF

    return  isValid
# EndSub


def setCardType(ccNum):
    card = 'Not Valid'
    if ccNum[0:2] == '37':
        card = 'Amex'
    elif ccNum [0] == '4':
        card = 'Visa'
    elif ccNum[0] == '5':
        card = 'Mastercard'
    elif ccNum[0] == '6':
        card = 'Discover'
    # EndIF

    return card

# EndSub


def displayResults(num, isValid, name):
    if name != 'Not valid':
        message =  '\nThe ' + name + ' credit card ' + num
        if isValid == True:
            message = message + 'is valid\n'
        else:
            message = message + 'is invalid\n'
        print(message)
    else:
        print('The card number' + num + 'is not valid')

# EndSub


#########################################################
#
#                       MAIN
#
#########################################################

Main()
