"""
    Program: CrapsGame
    File: CrapsGame.py
    Author: James Anderton
    Date: 21-Sep-2017
    Purpose: A simple craps game based on a random number generator
    Rules:
            -Roll to random dice (I know we have not done how to do random number generation yet, but it is not hard
            in Python (refer to page 245 dice.py....but remember you are not to do math in a print statement).
            -If the first roll is 7 or 11 the game ends and you win; OR if the first roll is 2, 3, 12 the game
            ends and you lose; OR if you roll a 4, 5, 6, 8, 9, 10 this is called the point and the game continues.
            -If a point was rolled in step 2 ...continue to roll until one of two things happen: if the user rolls
            a 7 the game ends and they lose; OR if they roll their point again before rolling a 7 the game ends
            and they win.
            -Program should run for as many full games as they want to play.
"""

# including this library for the dice generator
import random

#########################################################
#
#   SUB: showMenu
#
#########################################################
def showMenu():
    menuChoice = "Y"  # Used to get loop started
    games = 0
    winCount =0
    while True:
        try:
            while menuChoice == "Y" or menuChoice == "N":
                # Show the Menu
                print()
                print("Craps Game")
                print("==================================")
                print()
                print("You have won", winCount, "out of", games, "games.")
                menuChoice = input("Press Y to Start or N to Exit").capitalize()
                rollNum = 1
                if menuChoice == "Y":
                    die1, die2 = generateDie()
                    print("\tRoll ",rollNum, ":", die1,die2)

                    newWin, point = firstRoll(die1, die2, rollNum)

                    if newWin >0:
                        winCount +=newWin
                        games += 1
                        continue
                    elif newWin == -1:
                        games += 1
                        continue
                    else:
                        # ***Stage 2***
                        while newWin == 0:
                            newWin = 0
                            rollNum += 1
                            die1, die2 = generateDie()
                            print("\tRoll #", rollNum, ":",die1, die2)
                            newWin += nextRoll(die1, die2, rollNum, point)
                            if newWin > 0:
                                winCount += newWin
                                games += 1
                                break
                            elif newWin == -1:
                                games += 1
                                break

                        # EndWhile
                    # EndIf
                elif menuChoice == "N":
                    print("==================================")
                    print()
                    print("You have won", winCount, "out of", games, "games.")
                    print("Exiting...")
                    exit(0)
                else:
                    print("Please type in a valid choice (Y/N). \n")
                    showMenu()
                # EndIf
            # EndWhile

        except ValueError:
            print("Please type in a valid choice (Y/N). \n")
        # EndTry
    # EndWhile
# EndSub


#########################################################
#
#   SUB: generateDie
#
#########################################################
def generateDie():
    num1 = random.randrange(1, 6)
    num2 = random.randrange(1, 6)
    return num1, num2
# EndSub


#########################################################
#
#   SUB:firstRoll
#   REQUIRES: die1, die2, rollNum
#
#########################################################
def firstRoll(die1, die2, rollNum):
    totalDie = die1 + die2
    win =0
    point = 0
    if rollNum == 1 and totalDie == 7 or totalDie == 11:
        print("You Win!")
        print("==================================")
        print()
        win = 1
    elif rollNum == 1 and totalDie == 2 or totalDie == 3 or totalDie == 12:
        print("You Lose")
        print("==================================")
        print()
        win = -1
    elif rollNum == 1 and totalDie == 4 or totalDie ==  5 or totalDie == 6 or totalDie == 8 \
            or totalDie == 9 or totalDie == 10:
        # continue to second roll
        win = 0
        point = totalDie
    # EndIf

    return win, point
# EndSub


#########################################################
#
#   SUB: nextRoll
#   REQUIRES: die1, die2, rollNum, point
#
#########################################################
def nextRoll(die1, die2, rollNum, point):
    totalDie = die1 + die2
    win = 0
    if rollNum > 1 and totalDie == 7:
        print("You Lose")
        print("==================================")
        print()
        win = -1
    elif rollNum > 1 and totalDie == point:
        print("Point!")
        print("==================================")
        print()
        win = 1
    # EndIf

    return win
# EndSub


#########################################################
#
#                       RUNNER
#
#########################################################

showMenu()
