#
#     Program: NameFinder
#     File: NameFinder.py
#     Author: James Anderton
#     Date: 12-OCT-2017
#     Purpose: A program that allows a user to manipulate the top 200
#               boys and girls names in popularity
#
#########################################################
#
#   SUB: Main
#
#########################################################
def Main():
    another = 'Y'  # Used to get loop started

    while another == 'Y':
     choose = Menu()
     print(choose)

     temp = input('Do you wish to continue? (Enter Y for yes: ')
     another = temp[0].upper()

    #
    # girlFile = open('GirlNames.txt', 'r')
    # boyFile = open('BoyNames.txt', 'r')
    #
    # girls = girlFile.readlines()
    # boys = boyFile.readlines()
    #
    # girlFile.close()
    # boyFile.close()
    #
    # #Print Girls
    # index = 0
    # while index < len(girls):
    #     girls[index] = girls[index].rstrip('\n')
    #     index +=1
    # print(girls)
    #
    # #Boys
    # index = 0
    # while index < len(boys):
    #     boys[index] = boys[index].rstrip('\n')
    #     index +=1
    # print(boys)
    #
    # print(boys[0])
    # print(boys[-1])
    # print(boys[-3])
    # boysName = 'Elijah'
    # itemIndex = boys.index(boysName)
    #
    # if boysName in boys:
    #     print('Found')
    #     print(boysName, 'is the', (itemIndex +1), 'most popular name.')
    #
    # boys.append('Harrison')
    # boysName = 'Harrison'
    # itemIndex = boys.index(boysName)
    #
    # if boysName in boys:
    #     print('Found')
    #     print(boysName, 'is the', (itemIndex + 1), 'most popular name.')
    #
    # print(boys[2:5]) #prints 2, 3, and 4 but not 5
    # print(boys[198:]) #prints from 198 onwards
    # print(boys[:4]) #prints first 4 names
    #
    # outBoys = open('BoysNames2.txt', 'w+')
    # for names in boys:
    #     outBoys.write(names + '\n')
    # outBoys.close()
    #
    # outGirls = open('GirlsNames2.txt', 'w+')
    # for names in girls:
    #     outGirls.write(names + '\n')
    # outGirls.close()
    #
    # print(len(girls))
    # print(len(boys))
    #
    # boys.remove('James')
    # if 'James' in boys:
    #     print('found')
    # else:
    #     print('not found')
    #
    # boys.insert(16, 'James')
    # if 'James' in boys:
    #     print('found')
    # else:
    #     print('not found')

# EndSub

#########################################################
#
#   SUB: Menu
#
#########################################################
def Menu():

    # Show the Menu
    print("Name My Kid Generator")
    print("==================================")
    print("\t(F)ind a name")
    print("\t(I)ndex of name")
    print("\t(P)rint the 200 most popular names")
    print("\t(T)op ten names")
    print("\t(A)dd a name at an index number")
    print("\t(E)nd list append name")
    print("\t(R)emove a name")
    print("\t(S)ort and display")
    print("\tRe(V)erse the list")
    print("\t(W)rite the file")
    print("\t(C)opy file")
    print()

    tempChoice = input('Choose a menu item: ')
    choice = tempChoice[0].upper()

    return choice

# EndSub


#########################################################
#
#                       MAIN
#
#########################################################

#Menu()
Main()
