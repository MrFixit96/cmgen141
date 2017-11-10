# with open('writeStuff', 'w') as morePy:
#     morePy.write('test')
#     morePy.seek(0)
#     morePy.write('R')
#     print(morePy)

# with open("usdeclar.txt", 'r') as rFile:
#     with open("usdeclar-dupe.txt", 'w') as wFile:
#         for line in rFile:
#             wFile.write(line)

# with open("Names.txt", 'r') as rFile:
#     aName = rFile.readline()
#     aName = aName.rstrip('\n') # Like Chomp
#     print(aName)

with open("Names.txt", 'r') as rFile:
    friendName = rFile.readline()
    count =0
    total = 0
    while friendName != '':
        count += 1
        friendName = friendName.rstrip('\n')
        friendAge = rFile.readline()
        friendAge = int(friendAge.rstrip('\n'))
        total = total + friendAge
        print(friendName, friendAge)
        friendName = rFile.readline()
    avgAge = total/count
    print("The average age is: ", avgAge)