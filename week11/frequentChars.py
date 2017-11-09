#
#     Program: Sample
#     File: sample.py
#     Author: James Anderton
#     Date: 24-SEP-2017
#     Purpose: A Sample Program with a Menu
#
import string

#########################################################
#
#   SUB: Main
#
#########################################################
def Main():
    menuChoice = -99  # Used to get loop started

    while True:
        try:
            another = 'Y'  # Used to get loop started

            while another == 'Y':
                choose = Menu()
                print("Researching", choose)
                answer = getAnswer(choose)
                print('Your string was', choose, "and the most frequent character was:", answer)

                temp = input('Do you wish to continue? (Enter Y for yes: ')
                another = temp[0].upper()
                # EndWhile

            # EndWhile
            break

        except ValueError:
            print("Please type in a valid number. \n")
        # EndTry
    # EndWhile
# EndSub


#########################################################
#
#   SUB: Menu
#
#########################################################
def Menu():
    print('=== Most Frequent Character Finder ===')
    question = input('Type in the string you want to parse: ')

    return question


# EndSub


#########################################################
#
#   SUB: getAnswer
#   REQUIRES: choose
#
#########################################################
def getAnswer(choose):
    alphabet = list(string.ascii_lowercase)
    frequency=[]
    counter = 0
    for item in alphabet:
        counter = counter + 1
        if item in choose:
            frequency[counter] += 1

    print(alphabet)
    print(frequency)
# EndSub


#########################################################
#
#                       MAIN
#
#########################################################

Main()
