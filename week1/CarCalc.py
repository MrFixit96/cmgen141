'''
    Program: Car Calculator
    File: CarCalc.py
    Autho: James Anderton
    Date: 27-Aug-2017
    Purpose: This Program with take the input miles per hour, hours driven, vehicle mpg,
                and then calculate the distance travelled to the tenth of a mile, the
                amount of gas it took to one decimal place, and then display the distance
                and amount of gas used.
'''

# INPUT
print("===============================================================================================")
mph = int(input("Please enter the rate of speed in miles per hour: "))
timeDriven = float(input("Please enter the length of time spent driving in hours: "))
mpg = int(input("Please enter the efficiency of the car being driven in terms of Miles per Gallon: "))
print("===============================================================================================\n")

# PROCSESS
distance = float(mph * timeDriven)
gasUsed =  float(distance /mpg)


# OUTPUT
print("The car traveled " + str(format(distance, '.1f')) + " miles and used " + str(format(gasUsed, '.1f')) + " gallons of gas.")
