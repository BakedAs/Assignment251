import os, os.path;

def store (archiveDir, dirToBackup):
    if (os.path.exists(archiveDir) and os.path.isdir(archiveDir)):
        if (not os.path.exists(dirToBackup) or not os.path.isdir(dirToBackup)):
            print "Directory '"+dirToBackup+"' does not exist!";
            return;
    else:
        print "The backup archive has not been created! Use 'mybackup init' to initialise the directory before calling 'store'.";
