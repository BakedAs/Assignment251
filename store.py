import os, os.path, shutil, utilities;

def store (archiveDir, dirToBackup):
    if (os.path.exists(archiveDir) and os.path.isdir(archiveDir)):
        if (not os.path.exists(dirToBackup)):
            print "Directory '"+dirToBackup+"' does not exist!";
            return;
        elif (not os.path.isdir(dirToBackup)):
            print "File '"+dirToBackup+"' is not a directory!";
            return;
        for root, dirs, files in os.walk(dirToBackup):
            for name in files:
                backupFile(archiveDir, os.path.join(root, name));
    else:
        print "The backup archive has not been created! Use 'mybackup init' to initialise the directory before calling 'store'.";

        
def backupFile (archiveDir, fileName):
    hash = utilities.createFileSignature(fileName)[2];
    index = utilities.loadIndex(archiveDir);
    if (index.has_key(fileName)):
        #Check whether the file is already in the index
        #If so, remove the existing file
        canRemove = True;
        for key, value in index.items():
            if (value == hash and key != fileName):
                canRemove = False;#Another file exists with the same hash
        if (canRemove):
            os.remove(os.path.join(archiveDir, index[fileName]));
    index[fileName] = hash;
    shutil.copyfile(fileName, os.path.join(archiveDir, hash));
    utilities.saveIndex(archiveDir, index);
    
