#
#     Program: files
#     File: files.py
#     Author: James Anderton
#     Date: 24-SEP-2017
#     Purpose: A Sample Program with a Menu
#


#########################################################
#
#     SUB: writeFile
#
#########################################################

def writeFile():

    fobj = open('test.text', 'w')
    fobj.write('Hello Cruel World')
    fobj.close()
# EndSub


#########################################################
#
#     SUB: readFile
#
#########################################################
def readFile():

    fobj = open('usdeclar.txt', 'r')
    fileContents = fobj.read(100) #first hundred bytes
    print(fileContents)
    fileContents = fobj.read() #reads the whole file from where it left off
    print(fileContents)
    fobj.close()
# EndSub


#########################################################
#
#     SUB: readArray
#
#########################################################
def readArray():
    fobj = open('test2.txt', 'r')
    listMe = fobj.readlines()
    print(listMe)
    listMe[2] = 'I changed this one!'
    print(listMe)
    fobj.close()
# EndSub


#########################################################
#
#     SUB: readLine
#
#########################################################
def readLine():
    fobj = open('usdeclar.txt', 'r')
    output = fobj.readline()
    print(output)
    fobj.close()
# EndSub


#########################################################
#
#     SUB: writeLine
#
#########################################################
def writeLines():
    fobj = open('test2.txt', 'r')
    listMe = fobj.readlines()
    print(listMe)
    listMe[2] = 'I changed this one!'
    print(listMe)
    fobj.close()
    fobj = open('test2.txt', 'w')
    fobj.writelines(listMe)
    fobj.close()
# EndSub


#########################################################
#
#     SUB: usingWith
#
#########################################################
def usingWith():
    with open('usdeclar.txt', 'r') as myFile:
        fileContent = myFile.readline()
        print(fileContent)

        fileContent = myFile.readline()
        print(fileContent)

        fileContent = myFile.readline()
        print(fileContent)
# EndSub


#########################################################
#
#     SUB: readAll
#
#########################################################
def readAll():
    with open('usdeclar.txt', 'r') as myDeclare:
        for line in myDeclare:
            print(line, end='')
# EndSub


#########################################################
#
#     SUB: readChunks
#
#########################################################
def readChunks():
    AMT2READ = 100
    with open('usdeclar.txt', 'r') as myDeclare:
        fileContent = myDeclare.read(AMT2READ)
        while len(fileContent) > 0:
            print(fileContent, end='*')
            fileContent = myDeclare.read(AMT2READ)

# EndSub


#########################################################
#
#     SUB: readMoreChunks
#
#########################################################
def readMoreChunks():
    AMT2READ = 50
    with open('usdeclar.txt', 'r') as myDeclare:
        myDeclare.seek(200)
        fileContent = myDeclare.read(AMT2READ)
        print(fileContent)

        #RESET FILE DESCRIPTOR POSITION
        myDeclare.seek(0)
        fileContent = myDeclare.read(AMT2READ)
        print(fileContent)

# EndSub


#########################################################
#
#                      RUNNER
#
#########################################################

writeFile()
readFile()
readLine()
readArray()
writeLines()
usingWith()
readAll()
readChunks()
readMoreChunks()