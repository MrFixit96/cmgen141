#
#     Program: frequentChars
#     File: frequentChars.py
#     Author: James Anderton
#     Date: 09-Nov-2017
#     Purpose: A program to analyze a string and count the reoccurrences of a character and print out the ones with
#           the highest totals
#
import string

#Turn on and off debug printing here
#DEBUG = 1
DEBUG = 0

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
                print('Your string was', choose, "and the most frequent character(s) were:", answer)

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
    alphabet = []
    for item in list(string.ascii_lowercase):
        alphabet.append([item,0])
    # for num in range(len(alphabet)):
    #     frequency.append(0)

    for character in list(choose):
        for item in alphabet:
            if DEBUG == 1: print(item)
            if DEBUG == 1: print(character ,item[0])
            if str(item[0]).lower() == str(character).lower():
                if DEBUG == 1: print("Found One", character, item[0])
                item[1] +=1

    if DEBUG == 1: print(alphabet)
    temp = 0
    store =[]
    for item in alphabet:
        ####Made an adjustment to store most frequent characters in a list in case of a tie (mississippi)
        if item[1] > temp:
            temp = item[1]
            store.clear()
            store.append(item)
        elif item[1] == temp:
            store.append(item)

    return store

# EndSub


#########################################################
#
#                       MAIN
#
#########################################################

Main()
