__author__ = 'JoshBaker'
import os, os.path, utilities

def init(directory):
    try: #try to create the directory, throw OSError otherwise
        objectFilePath = os.path.join(directory, 'objects')
        indexFilePath = os.path.join(directory, 'index.txt')
        if not os.path.isdir(objectFilePath): #checks if the objects directory has been created. If not, creates directory
            os.makedirs(os.path.join(directory, 'objects'))
        if not os.path.exists(indexFilePath): #checks if the index file has been created. If not, creates file
            open(indexFilePath, 'a')
            utilities.saveIndex(directory, {})
            print "Archive directory created with subdirectory 'objects' and file 'index.txt' in " + directory
        else:
            print "Backup already intialised"
    except OSError: #throws an OSError if something went wrong with the creation of directory or files
        print "Error: Could not create directories or files"