'''
    Program: MultiplicationTable
    File: MultiplicationTable.py
    Author: James Anderton
    Date: 7-SEP-2017
    Purpose: A multiplication matrix using nested loops
'''

def multTable(maxNum):
    for row in range(1, maxNum + 1):
        for column in range(1, maxNum +1):
            value = row * column
            print(format(value, '8d'), end="")
        print()

def main():
    multTable(int(input("What is the maximum number to work with? ")))


main()