__author__ = 'FrancisGreatorex'
import os, os.path, shutil, utilities;

def store (archiveDir, dirToBackup, verbose=True):
    dirToBackup = os.path.abspath(dirToBackup);
    if (os.path.exists(archiveDir) and os.path.isdir(archiveDir)):
        if (not os.path.exists(dirToBackup)):
            print "Directory '"+dirToBackup+"' does not exist!";
            return;
        elif (not os.path.isdir(dirToBackup)):
            print "File '"+dirToBackup+"' is not a directory!";
            return;
        index = utilities.loadIndex(archiveDir);
        objectsDir = os.path.join(archiveDir, "objects");
        for root, dirs, files in os.walk(dirToBackup):
            for name in files:
                backupFile(objectsDir, os.path.join(root, name), index, verbose);
        utilities.saveIndex(archiveDir, index);
    else:
        print "The backup archive has not been created! Use 'mybackup init' to initialise the directory before calling 'store'.";

        
def backupFile (archiveDir, fileName, index, verbose=True):
    hash = utilities.createFileSignature(fileName)[2];
    if (index.has_key(fileName)):
        if (index[fileName] == hash):
            if (verbose):
                print "Backup file '"+fileName+"' already exists and is up-to-date; skipping.";
            return;
        #Check whether the file is already in the index
        #If so, remove the existing file
        canRemove = True;
        for key, value in index.items():
            if (value == hash and key != fileName):
                canRemove = False;#Another file exists with the same hash
        if (canRemove and os.path.exists(index[fileName])):
            os.remove(os.path.join(archiveDir, index[fileName]));
        if (verbose):
            print "Replacing backup file '"+fileName+"'";
    elif (verbose):
        print "Adding new file '"+fileName+"' to backup.";
    index[fileName] = hash;
    shutil.copyfile(fileName, os.path.join(archiveDir, hash));
    
