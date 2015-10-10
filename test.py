__author__ = 'JoshBaker'
import os, os.path, utilities

def test(directory):
    index = utilities.loadIndex(directory)
    objectFilePath = os.path.join(directory, 'objects')
    counter = 0
    for filename, hash in index.items():
        max = len(index.items())
        counter += 1
        if not os.path.exists(os.path.join(objectFilePath, hash)):
            print "This object does not have a matching file: " + hash
        elif max <= counter:
            print "All good here"
    # for filename, hash in index.items():


