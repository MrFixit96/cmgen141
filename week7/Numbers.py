#
#     Program: FileHead
#     File: FileHead.py
#     Author: James Anderton
#     Date: 12-OCT-2017
#     Purpose: A program that writes random numbers to a file and then
#               calculates the total sum of the numbers as well as the average.
#
import random

#########################################################
#
#   SUB: Main
#
#########################################################
def Main():
    another = 'Y'  # Used to get loop started

    while another == 'Y':
        #Do Work
        outNum = open('numbers.txt', 'w+')
        rNum = 0
        counter = 0
        while counter < 11:
            rNum = random.randint(1,100)
            print(rNum)
            outNum.write(str(rNum)+ "\n")
            counter += 1

        outNum.close()
        numIn = 0
        counter = 0
        inFile = open('numbers.txt', 'r')
        for line in inFile:
            temp = line.rstrip('\n')
            print(temp )
            numIn += int(temp)
            counter += 1
        avg = numIn / counter

        print("The total of all numbers in the file is:", numIn, "and the average is:", avg, ".")

        temp = input('Do you wish to continue? (Enter Y for yes: ')
        another = temp[0].upper()

# EndSub


#########################################################
#
#                      RUNNER
#
#########################################################

Main()
