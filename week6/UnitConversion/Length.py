#
#     Program: FallingDistance
#     File: Length.py
#     Author: James Anderton
#     Date: 03-OCT-2017
#     Purpose: a program to calculate the distance an object would fall given the duration of the fall.
#


#########################################################
#
#   SUB: getInput
#   PURPOSE: Take User Input for processing
#   RETURNS: fallingSecs
#
#########################################################
def getInput():
    print("Converting Units of Length")
    print("==================================")
    unitIn = input("Please enter the Scale of the unit being converted FROM "
                   "**ie. miles, yards, feet, length OR kilometers, meters, centimeters, length**: ")
    lengthIn = float(input("Please enter the length of the unit being converted: "))
    unitOut = input("Please enter the SI Scale of the unit being converted TO "
                    "**ie. miles, yards, feet, length OR kilometers, meters, centimeters, length**: ")

    return unitIn, unitOut, lengthIn
# EndSub


#########################################################
#
#   SUB: chooseScale
#   PURPOSE: take user input and decide which scale to use
#   REQUIRES: unitIn, unitOut, lengthIn
#
#########################################################
def chooseScale(unitIn, unitOut, lengthIn):
    try:
        if unitIn == "miles" or unitIn == "yards" or unitIn =="feet" or unitIn =="inches":
            newLength = breakdownStandard(lengthIn, unitIn)

        elif unitIn == "kilometers" or unitIn == "meters" or unitIn == "centimeters" or unitIn == "millimeters":
            newLength = breakdownMetric(lengthIn, unitIn)

        if unitOut == "miles" or unitOut == "yards" or unitOut =="feet" or unitOut =="inches":
            lengthOut = convertStandard(newLength, unitOut, unitIn)
        elif unitOut == "kilometers" or unitOut == "meters" or unitOut == "centimeters" or unitOut == "millimeters":
            lengthOut = convertMetric(newLength, unitOut, unitIn)
    except ValueError:
        print("Please enter a valid type.")

    return lengthOut
# EndSub


##########################################################
#
#   SUB: breakdownMetric
#   PURPOSE: a function that breaks down the user's Metric Scale
#           input into milimeters for conversion
#   REQUIRES: lengthIn, unitIn
#   RETURNS: length
#
##########################################################
def breakdownMetric(lengthIn, unitIn):
    length = 0.0
    try:
        if unitIn == "kilometers":
            length =  lengthIn /10000
        elif unitIn == "meters":
            length = lengthIn / 1000
        elif unitIn == "centimeters":
            length = lengthIn / 100
        elif unitIn == "millimeters":
            length = lengthIn
    except ValueError:
        print("Please choose a valid SI Unit.")

    return length
# EndSub


##########################################################
#
#   SUB: breakdownStandard
#   PURPOSE: a function that breaks down the user's SI Scale
#           input into length for conversion
#   REQUIRES: lengthIn, unitIn
#   RETURNS: length
#
##########################################################
def breakdownStandard(lengthIn, unitIn):
    length = 0.0
    try:
        if unitIn == "miles":
            length =  63360 / lengthIn
        elif unitIn == "yards":
            length = 36 / lengthIn
        elif unitIn == "feet":
            length = 12 / lengthIn
        elif unitIn == "inches":
            length = lengthIn
    except ValueError:
        print("Please choose a valid SI Unit.")


    return length
# EndSub


##########################################################
#
#   SUB: convertStandard
#   PURPOSE: a function that converts the user's SI Scale
#           input from length into the desired unit.
#   REQUIRES: length, unitOut
#   RETURNS: lengthOut
#
##########################################################
def convertStandard(length, unitOut, unitIn):
    lengthOut = 0.0
    if unitIn == "kilometers" or unitIn == "meters" or unitIn == "centimeters" or unitIn == "millimeters":
        length = length /.0393701

    try:
        if unitOut == "miles":
            lengthOut = length / 63360
        elif unitOut == "yards":
            lengthOut = length / 36
        elif unitOut == "feet":
            lengthOut = length / 12
        elif unitOut == "inches":
            lengthOut = length
        elif unitOut == "kilometers":
            lengthOut = length /39370.1
        elif unitOut == "meters":
            lengthOut = length /39.3701
        elif unitOut == "centimeters":
            lengthOut = length /.393701
        elif unitOut == "millimeters":
            lengthOut = length
    except ValueError:
        print("Please choose a valid SI Unit.")

    return lengthOut

# EndSub


##########################################################
#
#   SUB: convertMetric
#   PURPOSE: a function that converts the user's Metric Scale
#           input from length into the desired unit.
#   REQUIRES: length, unitOut
#   RETURNS: lengthOut
#
##########################################################
def convertMetric(length, unitOut, unitIn):
    lengthOut = 0.0
    if unitIn == "miles" or unitIn == "yards" or unitIn =="feet" or unitIn =="inches":
        length = length / 0.03937008

    try:
        if unitOut == "kilometers":
            lengthOut = length / 10000
            if unitIn == "miles":
                print("BUG: Not sure why my math isn't adding up.")
        elif unitOut == "meters":
            lengthOut = length / 1000
        elif unitOut == "centimeters":
            lengthOut = length / 10
        elif unitOut == "millimeters":
            lengthOut = length
        if unitOut == "miles":
            lengthOut = length / 1.609e+6
        elif unitOut == "yards":
            lengthOut = length / 0.00109361
        elif unitOut == "feet":
            lengthOut = length / 0.00328084
        elif unitOut == "inches":
            lengthOut = length
            
    except ValueError:
        print("Please choose a valid Metric Unit.")

    return lengthOut
# EndSub


#########################################################
#
#   SUB: displayResults
#   PURPOSE: Display the results of processing to the user
#   REQUIRES: distance, fallingSecs
#
#########################################################
def displayResults(lengthIn, lengthOut, unitIn, unitOut):
    print(lengthIn, unitIn, "is equal to", lengthOut, unitOut,".")

# EndSub