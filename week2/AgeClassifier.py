'''
    Program:Area Of Rectangles
    File: AreaOfRectangles.py
    Autho: James Anderton
    Date: 1-Sep-2017
    Purpose: From a user input for the length and width of two rectangles choose
                which has the larger area and return it to the screen.
'''
# INPUTS====================================================================
age = int(input("Please enter your age in years: "))

# PROCESSING====================================================================
age_level = ""
if age <=1:
    age_level = "infant"
elif age > 1 and age < 13:
    age_level = "child"
elif age >= 13 and age <20:
    age_level = "teenager"
elif age >= 20:
    age_level = "adult"
else:
    print("Please enter a valid number")


# OUTPUTS====================================================================
print("You are " + str(age) + " years old and that makes you a " + age_level + ".")