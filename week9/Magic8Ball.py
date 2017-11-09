#
#     Program: Magic8Ball
#     File: Magic8Ball.py
#     Author: James Anderton
#     Date: 26-Oct-2017
#     Purpose: a program that simulates a Magic 8 Ball, which is a fortune-telling toy that displays a
#       random response to a yes or no question. Using a text file named 8_ball_responses.txt.
#       The file contains 12 responses, such as "I don't think so'', "Yes, of course!", "I'm
#       not sure'', and so forth. The program should read the responses from the file into a list.
#       It should prompt the user to ask a question, then display one of the responses,
#       randomly selected from the list. The program should repeat until the user is ready to quit.
#     Requires: 8_ball_responses.txt
#
from random import randint

#########################################################
#
#   SUB: Main
#
#########################################################
def Main():
    another = 'Y'  # Used to get loop started
    INPUT_FILE = '8_ball_responses.txt'

    while another == 'Y':
        choose = Menu()
        print("Researching", choose)
        answer = getAnswer(choose, INPUT_FILE)
        print('You asked', choose, "and the Magic 8 Ball says:", answer)

        temp = input('Do you wish to continue? (Enter Y for yes: ')
        another = temp[0].upper()
    # EndWhile

# EndSub


#########################################################
#
#   SUB: Menu
#
#########################################################
def Menu():
    print('=== Magic 8 Ball ===')
    question = input('Type in the question you want to ask the Magic 8 Ball: ')

    return question

# EndSub


#########################################################
#
#   SUB: readFile
#
#########################################################
def readFile(fileName):

    file = open(fileName, 'r')
    lines = file.readlines()
    file.close()

    return lines

# EndSub


#########################################################
#
#   SUB: getAnswer
#
#########################################################
def getAnswer(choose, INPUT_FILE):
    index = randint(0,11)
    temp = readFile(INPUT_FILE)
    answer = temp[index].strip()

    return answer

# EndSub


#########################################################
#
#                       MAIN
#
#########################################################

Main()
