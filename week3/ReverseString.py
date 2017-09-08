'''
    Program: ReverseString
    File: ReverseString.py
    Author: James Anderton
    Date: 7-SEP-2017
    Purpose: to reverse a string's characters
'''

def strReverse(aString):
    revString = ''
    for ch in  aString:
        revString = ch + revString
    print(revString)

    revString2=""
    for item in ["bob", "tom", "mary"]:
        revString2 = " " + item + revString2
    print(revString2)
strReverse("Hello")
