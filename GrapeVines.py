'''
    Program: GrapeVines
    File: GrapeVines.py
    Autho: James Anderton
    Date: 24-Aug-2017
    Purpose: A small program to calculate the number of grape vines that can be planted in a row given the length
        distance between vines, and the room needed for the end post assemblies.
'''

# INPUTS
print("=========== Grape Vine Planting Calculator ===============")
rowLength = float(input("Enter the row length: "))
distBetween = float(input("Enter the distance between rows: "))
endPostFeet = float(input("Enter feet for end post: "))
print("============================================================")

# Processing
vines = int(rowLength - (2 * endPostFeet) / distBetween)

# Output
print("Vines: " + str(vines))
