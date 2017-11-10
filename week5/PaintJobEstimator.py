"""
    Program: PaintJobEstimator
    File: PaintJobEstimator.py
    Author: James Anderton
    Date: 21-SEP-2017
    Purpose: A program to calculate painting jobs based on:
        -square footage of area to be painted
        -coverage of the paint
        -gallons of paint needed
        -cost of paint per gallon
        -paint cost
        -labor hours required
        -labor cost
        -total cost of job
        -constant: LABOR_RATE = $3.00 a sq.
"""
#########################################################
#
#   SUB: paint
#   REQUIRES: totalArea
#
#########################################################
def paint(areaSqFt):
    while True:
        try:
            coverage = float(input("\t Enter the gallon coverage: "))
            numGallons = round((areaSqFt / coverage) + .5, 0)

        except ValueError:
            print("Sorry, I can't do that Dave!")
            continue
        else:
            break
        # EndTry
    # EndWhile

    print("\t===========================================================")
    print("\tPaint coverage per gallon:", coverage, "sq.ft.")
    print("\tTotal gallons needed for job:", numGallons)

    while True:
        try:

            galCost = float(input("\t Enter the cost of paint per gallon: "))
            paintCost = round((numGallons * galCost), 2)
        except ValueError:
            print("Sorry, I can't do that Dave!")
            continue
        else:
            break
        # EndTry
    # EndWhile

    print("\t===========================================================")
    print("\tCost per gallon: $", galCost)
    print("\tCost of the paint: $", format(paintCost, ',.2f'))

    return paintCost
# EndSub


#########################################################
#
#   SUB: labor
#   REQUIRES: areaToPaint
#
#########################################################
def labor(areaToPaint):
    LABOR_RATE = 3.00
    print("\t===========================================================")
    numPainters = int(input("\tHow many painters are on the job? "))
    painterPerHour = float(input("\tHow many Sq.Ft. can the painters cover per hour? "))

    areaPerPainter = (areaToPaint / numPainters)
    perEmpCost = areaPerPainter * LABOR_RATE
    totalCost = areaToPaint * LABOR_RATE

    print("\t===========================================================")
    print("\tCost per painter: $", format(perEmpCost, ',.2f'))
    print("\tTotal labor cost to paint: $", format(totalCost, ',.2f'))

    return totalCost
# EndSub


#########################################################
#
#   SUB: area
#
#########################################################
def area():
   # measurements = {"height": 0,"width": 0, "length": 0}
    while True:
        try:
            # for k,v in measurements:
             #   v = float(input("\tEnter the", k, "of the room: "))
            length = float(input("\t Enter the length of the room: "))
            width = float(input("\t Enter the width of the room: "))
            height = float(input("\t Enter the height of the room: "))
        except ValueError:
            print("Sorry, I can't do that Dave!")
            continue
        else:
            break
        # EndTry
    # EndWhile
    if length <= 0 or width <= 0 or height <= 0:
        print("You can't have negative length, width, or height.")
    # EndIf

    walls = round(2 * ((length * height) + (width * height)),2)
    ceiling = round(length * width, 2)
    areaTotal = walls + ceiling

    print("\t===========================================================")
    print("\tThe wall area is: ", format(walls, ',.2f'), 'sq.ft.')
    print("\tThe ceiling area is: ", format(ceiling, ',.2f'), 'sq.ft.')
    print("\tThe total paint area is: ", format(areaTotal, ',.2f'), 'sq.ft')

    return areaTotal

# EndSub

#########################################################
#
#   SUB: jobCost
#
#########################################################
def jobCost(labCost, materialCost):
    totalCost = labCost + materialCost
    print("\t===========================================================")
    print("\tTotal job cost: $", format(totalCost, ',.2f'))

    return totalCost
# EndSub


#########################################################
#
#    SUB: MAIN
#
#########################################################
def main():
    another = 'Y'

    while another == 'Y':
        print('** Dewey, Cheatem, and Howe Paint Estimator **')
        areaToPaint = area()
        materialCost = paint(areaToPaint)
        labCost = labor(areaToPaint)
        jobCost(labCost,materialCost)

        temp =input('Do you wish to calculate another job?\n Enter Y for yes or N for no')
        another = temp[0].upper()

# EndSub

#########################################################
main()