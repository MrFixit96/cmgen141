'''
    Program:Area Of Rectangles
    File: AreaOfRectangles.py
    Autho: James Anderton
    Date: 1-Sep-2017
    Purpose: From a user input for the length and width of two rectangles choose
                which has the larger area and return it to the screen.
'''
# INPUTS====================================================================
r1Length = int(input("Please enter the length of Rectangle 1: "))
r1Width = int(input("Please enter the width of Rectangle 1: "))
r2Length = int(input("Please enter the length of Rectangle 2: "))
r2Width = int(input("Please enter the width of Rectangle 2: "))

# PROCESSING====================================================================
area1 = r1Length * r1Width
area2 = r2Length * r2Width

# OUTPUTS====================================================================
if area1 > area2:
    print("Rectangle 1 is larger")
else:
    print("Rectangle 2 is larger")