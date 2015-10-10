__author__ = 'JoshBaker'
import os, os.path, utilities

def test(directory):
    index = utilities.loadIndex(directory)
    objectFilePath = os.path.join(directory, 'objects')
    everythingIsFine = True
    for filename, hash in index.items():
        if not os.path.exists(os.path.join(objectFilePath, hash)):
            print "This object does not have a matching file: " + hash
            everythingIsFine = False
    if everythingIsFine:
        print "All good here"


