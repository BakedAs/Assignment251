__author__ = 'JoshBaker'
import os, os.path

def init(directory):
    try:
        objectFilePath = os.path.join(directory, 'objects')
        if not os.path.isdir(objectFilePath):
            os.makedirs(os.path.join(directory, 'objects'))
        indexFilePath = os.path.join(directory, 'index.txt')
        if not os.path.exists(indexFilePath):
            open(indexFilePath, 'a')
            print "Archive directory created with subdirectory 'objects' and file 'index.txt' in " + directory
        else:
            print "Backup already intialised"
    except OSError:
        print "Error: Could not create directories or files"