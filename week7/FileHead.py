#
#     Program: FileHead
#     File: FileHead.py
#     Author: James Anderton
#     Date: 12-OCT-2017
#     Purpose: A program that displays up to the first five lines of a file
#               preceded by the line number
#
#########################################################
#
#   SUB: Main
#
#########################################################
def Main():
    another = 'Y'  # Used to get loop started

    while another == 'Y':
     #Do Work
     lines = open('usdeclar.txt', 'r')
     count = 1
     while count <= 5:
        line = str(count)+ ":" + lines.readline()
        print(line)
        count += 1

     temp = input('Do you wish to continue? (Enter Y for yes: ')
     another = temp[0].upper()

# EndSub


#########################################################
#
#                      RUNNER
#
#########################################################

Main()
