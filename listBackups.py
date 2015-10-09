__author__ = 'JoshBaker'
import os, os.path, utilities


def list(directory, pattern=None):
    index = utilities.loadIndex(directory)
    if pattern is not None:
        pattern = pattern.lower()
        switch = True
        for key in index:
            keyLower = key.lower()
            if pattern in keyLower:
                print key
                switch = False
        if switch:
            print "No matches found"
    else:
        for key in index:
            print key