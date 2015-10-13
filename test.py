__author__ = 'JoshBaker'
import os, os.path, utilities

def test(directory, logger):
    index = utilities.loadIndex(directory)
    objectFilePath = os.path.join(directory, 'objects')
    everythingIsFine = True
    counter = 0
    erroneousPaths = []
    try: #Easier to ask for forgiveness than permission (EAFP) Checks the files to be iterated over exist
        for fileName in os.listdir(objectFilePath):
            filePath = os.path.join(objectFilePath, fileName)
            hash = utilities.createFileSignature(filePath)[2]
            if hash != fileName:
                logger.warn("This object's hash does not match its filename: " + str(hash)) #logs an unsuccessful run of test function
                everythingIsFine = False

        for filename, hash in index.items():
            if not os.path.exists(os.path.join(objectFilePath, hash)):
                erroneousPaths.append(filename)
                logger.warn("This file could not be found in the objects directory: " + hash) #logs an unsuccessful run of test function
                everythingIsFine = False
            else:
                counter += 1
    except OSError: #throws an error if the files do not exist
        print "Error: The file does not exist!"

    if everythingIsFine and len(erroneousPaths) < 1: #Logs the successful running of test function
        logger.info("All objects' hashes match their filename and all index entries exist as objects in the archive")
    logger.info("The number of valid index entries is: " + str(counter))
