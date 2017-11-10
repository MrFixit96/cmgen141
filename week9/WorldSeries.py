#
#     Program: WorldSeries
#     File: WorldSeries.py
#     Author: James Anderton
#     Date: 26-Oct-2017
#     Purpose: A program that lets the user enter the name of a
#       team, then displays the number of times that team has
#       won the World Series in the time period from 1903 through 2009.
#     Requires: WorldSeriesWinners.txt
#

#########################################################
#
#   SUB: Main
#
#########################################################
def Main():
    another = 'Y'  # Used to get loop started
    INPUT_FILE = 'WorldSeriesWinners.txt'

    while another == 'Y':
        choose = Menu()
        print("Researching", choose)
        count = getWinner(choose, INPUT_FILE)
        print('We found that the', choose, "won", count, "times between 1903 and 2009.")

        temp = input('Do you wish to continue? (Enter Y for yes: ')
        another = temp[0].upper()


# EndSub


#########################################################
#
#   SUB: Menu
#
#########################################################
def Menu():
    print('=== World Series Winners ===')
    team = input('Enter the city and name of the team you want to find out about: ')

    return team

# EndSub


#########################################################
#
#   SUB: readFile
#
#########################################################
def readFile(fileName):

    file = open(fileName, 'r')
    lines = file.readlines()
    file.close()

    return lines

# EndSub


#########################################################
#
#   SUB: getWinner
#
#########################################################
def getWinner(choose, INPUT_FILE):
    count = 0
    temp = readFile(INPUT_FILE)
    for item in temp:
        if choose == item.strip('\n'):
            count += 1
        # EndIf
    # EndFor

    return count

# EndSub


#########################################################
#
#                       MAIN
#
#########################################################

Main()
