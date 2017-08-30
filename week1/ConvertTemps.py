'''
    Program: Temperature Converter
    File: ConvertTemp.py
    Autho: James Anderton
    Date: 27-Aug-2017
    Purpose: This Program will take a temperature inputted in Celsius and convert it to Fahrenheit.
'''

# INPUT
print("===============================================================================================")
tempC = float(input("Please enter the tempurature in Celsius to convert from: "))
print("===============================================================================================\n")

# PROCSESS
tempF = 9/5 * tempC + 32

# OUTPUT
print(str(tempC) + " Celsius converted to Fahrenheit is  " + str(format(tempF, '.1f')))
