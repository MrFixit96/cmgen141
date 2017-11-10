'''
    Program:HotDogCalculator
    File: HotDogCalculator.py
    Autho: James Anderton
    Date: 31-Aug-2017
    Purpose: From a user input for the numer of people determin the
            packages of hot dogs and buns needed for ta single
            serving for each attendee and any leftovers
            - packages of hot dogs contain 10
            - packages of hot dog buns contain 8
'''
# INPUTS====================================================================
print("=============James\' Hot Dog Calculator==================")
numPeeps = int(input("Enter the number of attendees: "))
numServings = int(input("How many servings per: "))
totalServings = numPeeps * numServings

BUNS = 8
DOGS = 10

# PROCESSING ================================================================
######DOGS_SECTION
numOfItems = totalServings // DOGS
needMoreItems = totalServings % DOGS
if needMoreItems > 0:
    numOfItems += 1
    leftOverDogs = DOGS - needMoreItems
else:
    leftOverDogs = 0

numOfDogs = numOfItems * DOGS

######BUNS_SECTION
numOfItems = totalServings // BUNS
needMoreItems = totalServings % BUNS
if needMoreItems > 0:
    numOfItems += 1
    leftOverBuns = BUNS - needMoreItems
else:
    leftOverBuns = 0
numOfBuns = numOfItems * BUNS

# OUTPUT=======================================================================
print("Number of dogs " + str(numOfDogs))
print("Number of leftover dogs " + str(leftOverDogs))
print("Number of buns " + str(numOfBuns))
print("Number of leftover buns " + str(leftOverBuns))