'''
    Program: MathQuizzer
    File: MathQuizzer.py
    Author: James Anderton
    Date: 14-SEP-2017
    Purpose: A program to teach integer math to you
            students:
                -Numbers confined to 0-9 (division quotients will wall into this range
                -No Negative numbers are calculated
                -Division by zero should not occur
'''
import random #needed to generate random numbers


#########################################################
#
#   SUB: generateNum
#
#########################################################
def generateNum():
    number = random.randrange(0, 9)
    return number


# EndSub

#########################################################
#
#   SUB: showMenu
#
#########################################################
def showMenu():
    # Show the Menu
    print("Welcome to the Math Quizzer")
    print("==================================")
    print("\t1. Addition")
    print("\t2. Subtraction")
    print("\t3. Multiplication")
    print("\t4. Division")
    print()

    while True:
        try:
            # get the next choice
            choice = int(input("Select option: "))
            while choice < 1 or choice > 4:
                print('That is not a valid choice')
                choice = int(input('Please re-enter a choice'))

        except ValueError:
            print("Sorry, I didn't understand that")
            continue
            # returns to start of loop
        else:
            # Choice was parsed correctly
            # Exit the loop
            break
        # EndTry
    # EndWhile
    return choice

# EndSub
#########################################################
#
#   SUB: addition
#
#########################################################
def addition(num1, num2):
    answer = (num1 + num2)
    print(num1, "+" ,num2)
    return answer
# EndSub

#########################################################
#
#   SUB: subtraction
#
#########################################################
def subtraction(num1, num2):
    # making sure there's no negative numbers
    if num1 > num2:
        temp = num1
        num1 = num2
        num2 = temp
    # EndIf

    answer = (num1 - num2)
    print(num1, "-" ,num2)
    return answer

# EndSub


#########################################################
#
#   SUB: multiplication
#
#########################################################
def multiplication(num1, num2):
    answer = (num1 * num2)
    print(num1, "x" ,num2)
    return answer

# EndSub


#########################################################
#
#   SUB: division
#
#########################################################
def division(num1, num2):
    # if  num1 < num2:
    #     temp = num1
    #     num1 = num2
    #     num2 = temp
    # if num1 == 0 or num2 == 0:
    #     num1,num2 = generateNum()
    #
    # answer = (num1 // num2)
    # print(num1, "/" ,num2)

    if num1 == 0:
        num1 = 1
    # EndIf

    dividend = num1 * num2
    print(dividend, '/', num1, '=')
    answer = num2

    return answer

# EndSub

#########################################################
#
#       SUB: getUserAnswer
#
#########################################################
def getUserAnswer(correctAns):
    localCorrectAns = int(correctAns)
    correct = 0
    while True:
        try:
            answer = int(input('Enter answer: '))
        except ValueError:
            print('Sorry... That is not a whole number')
            continue
        else:
            break
        # EndTry
    # EndWhile
    if localCorrectAns == answer:
        print('Correct! Good Job...')
        correct = 1
    else:
        print('Im sorry, that is not correct')
        correct = 0
    # EndIf
    return correct
# EndSub

#########################################################
#
#       SUB: MAIN
#
#########################################################
def main():
    playAgain = 'Y'
    counter = 0
    numCorrect = 0
    while playAgain == 'Y' or playAgain == 'y':
        choice = showMenu()

        counter += 1

        num1 =  int(generateNum())
        num2 = int(generateNum())

        if choice == 1:
            correctAnswer = addition(num1, num2)
        elif choice == 2:
            correctAnswer = subtraction(num1, num2)
        elif choice == 3:
            correctAnswer = multiplication(num1, num2)
        elif choice == 4:
            correctAnswer = division(num1, num2)
        else:
            print("Please choose 1-4 ")
            choice = showMenu()
        # EndIf

        addCorrect = getUserAnswer(correctAnswer)
        numCorrect += addCorrect
        playAgain = input("Enter Y to continue, other input quits: ")

    print('You have', numCorrect, 'out of', counter)
    # EndWhile
# EndSub

###################******RUNNER*****######################################
main()
