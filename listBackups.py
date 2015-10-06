__author__ = 'JoshBaker'
import os, os.path, utilities

def list(directory, pattern = None):
    index = utilities.loadIndex(directory)
    if pattern != None:
        pattern = pattern.lower()
        for key in index:
            keyLower = key.lower()
            if pattern in keyLower:
                print key
    else:
        for key in index:
            print key
