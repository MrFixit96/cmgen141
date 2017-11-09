#
#     Program: KineticEnergy
#     File: Mass.py
#     Author: James Anderton
#     Date: 03-Oct-2017
#     Purpose: program to determine the kinetic energy of an object
#               KE= 1/2 mv2
#
#########################################################
#
#   SUB: displayResults
#   PURPOSE: Display the results of processing to the user
#   REQUIRES: distance, fallingSecs
#
#########################################################
def displayResults(mass, velocity, energy):
    print("An object weighing", mass, "kilograms and traveling at a velocity of", velocity , "meters/sec has a kinetic"
          "energy of", energy, "Joules")

# EndSub


##########################################################
#
#   SUB: kineticEnergy
#   PURPOSE: a function named kinetic_energy that accepts an object's mass (in kilograms)
#               and velocity (in meters per second) as arguments. The function should return the amount
#               of kinetic energy that the object has..
#   REQUIRES: fallingSecs
#   RETURNS: distance
#
##########################################################
def kineticEnergy(mass, velocity):

    energy = (mass * velocity ** 2) / 2

    return energy
# EndSub


#########################################################
#
#   SUB: getInput
#   PURPOSE: Take User Input for processing
#   RETURNS: fallingSecs
#
#########################################################
def getInput():
    print("Kinetic Energy Calculation")
    print("==================================")
    mass = int(input("Please enter the mass of the object in kilograms: "))
    velocity = int(input("Please enter the velocity of the object in meters per second: "))

    return mass, velocity
# EndSub