#!/usr/bin/env python2
__author__ = 'FrancisGreatorex'
import sys, os, init, listBackups, store, restore, test;
import logging, logging.handlers;

PROGRAM_NAME="myBackup";
LOG_FILENAME=PROGRAM_NAME + '.log';

#Define archive location
archiveDir = os.path.expanduser("~/myArchive");

def initLogger():
    loggerPath = os.path.join(archiveDir, LOG_FILENAME);
    logger = logging.getLogger(PROGRAM_NAME);
    logger.setLevel(logging.DEBUG);
    #====================================================================================
    # FILE-BASED LOG

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #formatter = logging.Formatter('%(levelname)s - %(message)s')

    # LOGFILE HANDLER - SELECT ONE OF THE FOLLOWING TWO LINES
    if os.path.exists(archiveDir):
        fh = logging.FileHandler(loggerPath)                          # Continuous Single Log
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    
    #=================================================================================
    # CONSOLE HANDLER - can have a different loglevel and format to the file-based log 
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(message)s')     # simpler display format
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger;

def main (argv):
    logger = initLogger();
    
    if (len(argv) == 0):
        print "Missing argument. Options: init, store, list, test, get, restore";
    elif (argv[0] == "init"):
        init.init(archiveDir);
    elif (argv[0] == "store"):
        if (len(argv) < 2):
            print "Usage: mybackup store <directory>";
        else:
            store.store(archiveDir, argv[1], logger);
    elif (argv[0] == "list"):
        if (len(argv) < 2):
            listBackups.list(archiveDir)
        else:
            listBackups.list(archiveDir, argv[1])
    elif (argv[0] == "get"):
        if (len(argv) < 2):
            print "Usage: mybackup get <pattern>";
        else:
            restore.getFile(archiveDir, argv[1]);
    elif (argv[0] == "restore"):
        if (len(argv) < 2):
            restore.restoreAll(archiveDir)
        else:
            restore.restoreAll(archiveDir, argv[1])
    elif (argv[0] == "test"):
        test.test(archiveDir, logger)
    else:
        print "Unknown option: "+argv[0];

if __name__ == "__main__":
   main(sys.argv[1:])
