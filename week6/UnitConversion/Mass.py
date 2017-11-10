#
#     Program: Mass
#     File: Mass.py
#     Author: James Anderton
#     Date: 03-OCT-2017
#     Purpose: a program to convert the scale of the mass of one object to another (ie. standard to metric)
#


#########################################################
#
#   SUB: getInput
#   PURPOSE: Take User Input for processing
#   RETURNS: fallingSecs
#
#########################################################
def getInput():
    print("Converting Units of Mass")
    print("==================================")
    unitIn = input("Please enter the Scale of the unit being converted FROM "
                   "**ie. pounds, ounces OR kilograms, grams**: ")
    lengthIn = float(input("Please enter the mass of the unit being converted: "))
    unitOut = input("Please enter the Scale of the unit being converted TO "
                    "**ie. pounds, ounces OR kilograms, grams**: ")

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
        if unitIn == "pounds" or unitIn == "ounces":
            newLength = breakdownStandard(lengthIn, unitIn)

        elif unitIn == "kilograms" or unitIn == "grams":
            newLength = breakdownMetric(lengthIn, unitIn)

        if unitOut == "pounds" or unitOut == "ounces":
            lengthOut = convertStandard(newLength, unitOut, unitIn)
        elif unitOut == "kilograms" or unitOut == "grams":
            lengthOut = convertMetric(newLength, unitOut, unitIn)
    except ValueError:
        print("Please enter a valid type.")

    return lengthOut


# EndSub


##########################################################
#
#   SUB: breakdownMetric
#   PURPOSE: a function that breaks down the user's Metric Scale
#           input into grams for conversion
#   REQUIRES: massIn, unitIn
#   RETURNS: mass
#
##########################################################
def breakdownMetric(massIn, unitIn):
    mass = 0.0
    try:
        if unitIn == "kilograms":
            mass = massIn / 1000
        elif unitIn == "grams":
            mass = massIn
    except ValueError:
        print("Please choose a valid SI Unit.")

    return mass


# EndSub


##########################################################
#
#   SUB: breakdownStandard
#   PURPOSE: a function that breaks down the user's SI Scale
#           input into ounces for conversion
#   REQUIRES: massIn, unitIn
#   RETURNS: mass
#
##########################################################
def breakdownStandard(massIn, unitIn):
    mass = 0.0
    try:
        if unitIn == "pounds":
            mass = 16 / massIn
        elif unitIn == "ounces":
            mass = massIn
    except ValueError:
        print("Please choose a valid SI Unit.")

    return mass


# EndSub


##########################################################
#
#   SUB: convertStandard
#   PURPOSE: a function that converts the user's SI Scale
#           input from mass into the desired unit.
#   REQUIRES: mass, unitOut
#   RETURNS: massOut
#
##########################################################
def convertStandard(mass, unitOut, unitIn):
    massOut = 0.0
    if unitIn == "kilograms" or unitIn == "grams":
        mass = mass * 0.035274
        print("DEBUG:", mass)
    try:
        if unitOut == "pounds":
            massOut = mass / 16
        elif unitOut == "ounces":
            massOut = mass
        elif unitOut == "kilograms":
            massOut = mass / 0.453592
        elif unitOut == "grams":
            massOut = mass / 28.3495
    except ValueError:
        print("Please choose a valid SI Unit.")

    return massOut


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
def convertMetric(mass, unitOut, unitIn):
    massOut = 0.0
    if unitIn == "pounds" or unitIn == "ounces":
        mass = mass * 28.3495
        print("DEBUG:", mass)
    try:
        if unitOut == "kilograms":
            massOut = mass / 1000
            if unitIn == "grams":
                print("BUG: Not sure why my math isn't adding up.")
        elif unitOut == "grams":
            massOut = mass
        if unitOut == "pounds":
            massOut = mass / 0.00220462
        elif unitOut == "ounces":
            massOut = mass / 0.035274

    except ValueError:
        print("Please choose a valid Metric Unit.")

    print("DEBUG:", massOut)
    return massOut


# EndSub


#########################################################
#
#   SUB: displayResults
#   PURPOSE: Display the results of processing to the user
#   REQUIRES: distance, fallingSecs
#
#########################################################
def displayResults(massIn, massOut, unitIn, unitOut):
    print(massIn, unitIn, "is equal to", round(massOut, 2), unitOut, ".")

    # EndSub