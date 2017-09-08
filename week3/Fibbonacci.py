'''
    Program: Fibbonacci
    File: Fibbonacci.py
    Author: James Anderton
    Date: 7-Sept-2017
    Purpose: A small program to generate Fibbonacci Numbers
'''

def fibbonacci(limit):
    num1 = 1
    num2 = 1
    print("=============== Fibbonacci Numbers ===================")
    print(num1, end=" ")

    while num2 <= limit:
        print(num2, end=" ")
        newNum = num1 + num2
        num1 = num2
        num2 = newNum

# Input



# Process
fibbonacci(input("Enter a number for the top end limit"))


# Output