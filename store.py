__author__ = 'FrancisGreatorex'
import os, os.path, shutil, utilities;

def store (archiveDir, dirToBackup, logger):
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
                try:
                    backupFile(objectsDir, os.path.join(root, name), index, logger);
                except OSError as (errno, strerror, filename):
                    print "Failed to backup file '"+name+"': "+strerror;
                except IOError as (errno, strerror):
                    print "Failed to backup file '"+name+"': "+strerror;
        utilities.saveIndex(archiveDir, index);
    else:
        print "The backup archive has not been created! Use 'mybackup init' to initialise the directory before calling 'store'.";

        
def backupFile (archiveDir, fileName, index, logger):
    fileHash = utilities.createFileSignature(fileName)[2];
    if (index.has_key(fileName)):
        if (index[fileName] == fileHash):
            logger.debug("Backup file '"+fileName+"' already exists and is up-to-date; skipping.");
            return;
        #Check whether the file is already in the index
        #If so, remove the existing file
        canRemove = True;
        for key, value in index.items():
            if (value == fileHash and key != fileName):
                canRemove = False;#Another file exists with the same hash
        if (canRemove and os.path.exists(index[fileName])):
            os.remove(os.path.join(archiveDir, index[fileName]));
        logger.info("Replacing backup file '"+fileName+"'");
    logger.info("Adding new file '"+fileName+"' to backup.");
    index[fileName] = fileHash;
    shutil.copyfile(fileName, os.path.join(archiveDir, fileHash));
    
