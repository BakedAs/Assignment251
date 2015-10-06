__author__ = 'JoshBaker'
import os, os.path, utilities

def list(directory, pattern = None):
    index = utilities.loadIndex(directory)
    pattern = pattern.lower()
    for key in index:
        keyLower = key.lower()
        if pattern == None:
            print key
        elif pattern in keyLower:
            print key
