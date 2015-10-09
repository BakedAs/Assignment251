__author__ = 'JoshBaker'
import os, os.path, utilities

def test(directory):
    index = utilities.loadIndex(directory)
    for key in index:
        print "fuck this"