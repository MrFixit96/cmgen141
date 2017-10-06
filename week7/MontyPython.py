with open('montyPython.jpg', 'rb') as rBinFile:
    with open('monty-dupe.jpg', 'wb') as wBinFile:
        chunk = 4096
        rBFChunk = rBinFile.read(chunk)
        while len(rBFChunk) > 0:
            wBinFile.write(rBFChunk)
            rBFChunk =  rBinFile.read(chunk)

print(rBinFile.closed)
print(wBinFile.closed)