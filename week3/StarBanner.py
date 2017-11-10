'''
    Program: StarBanner
    File: StarBanner.py
    Author: James Anderton
    Date: 7-Sept-2017
    Purpose: To print out a series of stars
'''


def dispBanner(starCount):
    for count in range(starCount):
        print("*", end='')
    print()

dispBanner(99)
