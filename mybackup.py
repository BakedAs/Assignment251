#!/usr/bin/env python2

import sys, os, init, listBackups, store;

#Define archive location
archiveDir = os.path.expanduser("~/myArchive");

def main (argv):
    if (len(argv) == 0):
        print "Missing argument. Options: init, store, list, test, get, restore";
    elif (argv[0] == "init"):
        init.init(archiveDir);
    elif (argv[0] == "store"):
        if (len(argv) < 2):
            print "Usage: mybackup store <directory>";
        else:
            store.store(archiveDir, argv[1]);
    elif (argv[0] == "list"):
        if (len(argv) < 2):
            listBackups.list(archiveDir)
        else:
            listBackups.list(archiveDir, argv[1])
    else:
        print "Unknown option: "+argv[0];

if __name__ == "__main__":
   main(sys.argv[1:])
