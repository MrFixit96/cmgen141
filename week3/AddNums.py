'''
    Program: AddNums
    File: AddNums.py
    Author: James Anderton
    Date: 7-SEP-2017
    Purpose: A program to create an example of a running total or accumulator
'''

def addNums(startNum, endNum):
    total = 0
    for nums in range(startNum, endNum + 1):
        total += nums
    print(total)

addNums(1,3)
