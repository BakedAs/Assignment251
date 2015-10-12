__author__ = 'JoshBaker'
import os, os.path, utilities

def test(directory):
    index = utilities.loadIndex(directory)
    objectFilePath = os.path.join(directory, 'objects')

    everythingIsFine = True
    counter = 0
    erroneousPaths = []

    for fileName in os.listdir(objectFilePath):
        filePath = os.path.join(objectFilePath, fileName)
        hash = utilities.createFileSignature(filePath)[2]
        if hash != fileName:
            print "This file does not have a matching filename: " + str(hash)
            everythingIsFine = False

    for filename, hash in index.items():
        if not os.path.exists(os.path.join(objectFilePath, hash)):
            erroneousPaths.append(filename)
            print "This object does not have a matching file: " + hash
            everythingIsFine = False
        else:
            counter += 1

    if everythingIsFine and len(erroneousPaths) < 1:
        print "All objects have matching file and the file contents match the filenames"
        print "The number of valid files is: " + str(counter)
    else:
        print "These files do not have matching objects: "
        for fileName in erroneousPaths:
            print fileName
        print "The number of valid files is: " + str(counter)