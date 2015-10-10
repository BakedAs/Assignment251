__author__ = 'JoshBaker'
import os, os.path, utilities

def test(directory):
    index = utilities.loadIndex(directory)
    objectFilePath = os.path.join(directory, 'objects')
    print index
    # print objectFilePath
    for file in os.listdir(objectFilePath):
        # file.strip("/Users/JoshBaker/Documents/Repositories/Assignment251/.git/objects/")
        # print file
        for key in index:
            # print key
            if key in file:
                print "matching file"
