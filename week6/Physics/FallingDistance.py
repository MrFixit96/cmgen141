#
#     Program: FallingDistance
#     File: Length.py
#     Author: James Anderton
#     Date: 03-OCT-2017
#     Purpose: a program to calculate the distance an object would fall given the duration of the fall.
#

#########################################################
#
#   SUB: displayResults
#   PURPOSE: Display the results of processing to the user
#   REQUIRES: distance, fallingSecs
#
#########################################################
def displayResults(distance, fallingSecs):
    print("An object falling for", fallingSecs, "seconds would fall for a distance of", int(distance) , "meters.")

# EndSub


##########################################################
#
#   SUB: falling_distance
#   PURPOSE: a function named falling_distance that accepts an object's falling time (in seconds)
#               as an argument. The function should return the distance, in meters, that the object has
#               fallen during that time interval.
#   REQUIRES: fallingSecs
#   RETURNS: distance
#
##########################################################
def fallingDistance(fallingSecs):
    GRAVITY = 9.8
    distance = (GRAVITY * fallingSecs ** 2) / 2

    return distance
# EndSub


#########################################################
#
#   SUB: getInput
#   PURPOSE: Take User Input for processing
#   RETURNS: fallingSecs
#
#########################################################
def getInput():
    print("Falling Distance Calculation")
    print("==================================")
    fallingSecs = int(input("Please enter the duration of the fall in seconds: "))

    return fallingSecs
# EndSub