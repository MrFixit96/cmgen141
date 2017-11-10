#
#     Program: StatesAndCaps
#     File: StatesAndCaps.py
#     Author: James Anderton
#     Date: 09-Nov-2017
#     Purpose: program will list states and capitals, list only states, look up
#             capitals based on states, and play a game.
#
import random

#GLOBALS
STATE_CAPS = 1
STATES_ONLY = 2
CAPITALS = 3
GAME = 4
QUIT = 5
tries = 0
score = 0


#########################################################
#
#   SUB: Main
#
#########################################################
def Main():
    global tries
    global score
    choice = 0

    #initialize copy of the states dictionary
    myStates = statesCapitals()

    while choice != QUIT:
        choice = setMenuChoice()
        if choice == STATE_CAPS:
            printList(myStates)
        elif choice == STATES_ONLY:
            printList(list(myStates.keys()))
        elif choice == CAPITALS:
            states = statesCapitals()
            showChosenCapital(states)
        elif choice == GAME:
            if len(myStates) > 0:
                tries += 1
                myStates = playGame(myStates)

            else:
                print('You have completed the game!')
                cont = input('Enter Y to reset the game, any other key to quit: ')
                if cont == 'Y' or cont == 'y':
                    myStates = statesCapitals()
                    score = 0
                    tries = 0
                else:
                    choice = QUIT
        else:
            choice = QUIT

# EndSub


#########################################################
#
#   SUB: printList
#
#########################################################
def printList(myList):
    for item in myList:
        print(item)

# ENDsub


#########################################################
#
#   SUB: Menu
#
#########################################################
def setMenuChoice():
    print('=== States and Capitals ===')
    print('1. List all states and capitals')
    print('2. List all the states')
    print('3. Look up a capital')
    print('4. Play a game')
    print('5. Quit')

    while True:
        choice = -1
        number = input('Enter your number choice: ')
        try:
            choice = int(number)
            if choice < STATE_CAPS or choice > QUIT:
                print('Sorry, input must be an integer between 1 and 5, try again!')
                continue
            break
        except ValueError:
            print('Thats not an integer')

    return choice
# EndSub


#########################################################
#
#   SUB: showChosenCapital
#
#########################################################
def showChosenCapital(states):
    print('What state do you want the capital of: ')
    userInput = input('Enter answer: ').capitalize()

    # dict.get tries to find input or prints the reply
    print(states.get(userInput, "State you input was not found, try again"))

# ENDsub


#########################################################
#
#   SUB: StatesCapitals
#
#########################################################
def statesCapitals():
    state = {'Illinois':'Springfield', 'Wisconsin':'Madison',
             'Florida':'Tallahasee', 'Michigan':'Lansing',
             'New Mexico':'Santa Fe', 'California':'Sacramento',
             'Washington':'Olympia', 'Georgia':'Atlanta'
             }

    return state

# ENDsub


#########################################################
#
#   SUB: playGame
#
#########################################################
def playGame(dictionary):

    global score
    global tries

    state = random.choice(list(dictionary))

    print('What is the capital of', str(state), "?") #Have to cast state to string because its a key object
    studentAnswer = input("Enter answer: ").capitalize()

    answer = str(dictionary[state]).capitalize() #This is the correct answer

    if studentAnswer == answer:
        print("Correct!")
        del dictionary[state] #Make sure not to repeat questions
        score +=1
        print("You got", score, "out of", tries, "tries")
    else:
        print('Sorry, wrong answer')
        print("You got", score, "out of", tries, "tries")
    # EndIF

    return dictionary

# ENDsub


#########################################################
#
#                       MAIN
#
#########################################################

Main()
