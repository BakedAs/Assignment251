#!/usr/bin/env python2

import sys;

def main (argv):
    if (len(argv) == 0):
        print "Missing argument. Options: init, store, list, test, get, restore";
    else:
        print "Unknown option: "+argv[0];
        
        
if __name__ == "__main__":
   main(sys.argv[1:])
