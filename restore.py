import os, os.path, shutil, utilities;

def restoreAll (archiveDir, path=None):
    index = utilities.loadIndex(archiveDir);
    if (path is None):#Restore to the original locations
        for filename, fileHash in index.items():
            restoreFile(archiveDir, fileHash, filename);
    else:        
        print "Attempting to restore to path "+path;
        path = os.path.abspath(path);
        for filepath, fileHash in index.items():
            dest = os.path.join(path, os.path.splitdrive(filepath)[1].lstrip(os.sep));
            destDir = os.path.dirname(dest);
            if not os.path.exists(destDir):
                os.makedirs(destDir);
            restoreFile(archiveDir, fileHash, dest);
    
def getFile (archiveDir, searchPattern):
    index = utilities.loadIndex(archiveDir);
    matches = [];
    
    #Find all the matching files.
    for name in index:
        if searchPattern in name:
            matches.append(name);
    
    if (len(matches) == 0):
        print "No matches found for pattern '"+searchPattern+"'";
    elif (len(matches) == 1):
        #Set the destination to the cwd and the filename to the old filename
        newDest = os.path.join(os.getcwd(), os.path.basename(matches[0]));
        restoreFile(archiveDir, index[matches[0]], newDest);
    else:
        #There's multiple entries matching the pattern. List them and let the user choose which one they want.
        print "Multiple entries found. Please select the one you wish to restore."
        i = 0;
        for name in matches:
            i+=1;
            print str(i)+": "+name;
        destName = None;
        while (destName == None):
            responseStr = raw_input("Enter your choice (q to cancel): ");
            try:
                if (responseStr.lower() == 'q'):
                    return;
                choice = int(responseStr);
                if (choice < 1 or choice > i):#If the choice was out of range
                    print "Invalid choice "+str(choice)+"! Please select again.";
                else:
                    destName = matches[choice-1];
            except ValueError:#If the response entered was not a number.
                print "Invalid response "+responseStr+"! Please select again.";
        #Set the destination to the cwd and the filename to the old filename
        newDest = os.path.join(os.getcwd(), os.path.basename(destName));
        restoreFile(archiveDir, index[destName], newDest);
        
def restoreFile (archiveDir, fileHash, dest, verbose=True):
    if (os.path.exists(dest)):
        while (True):
            response = raw_input("File already exists at "+dest+". Overwrite? (y/n)").lower();
            if (response == 'y' or response == 'yes'):
                break;#User wishes to overwrite existing file. Break out of the loop and continue the function.
            elif (response == 'n' or response == 'no'):
                return;#User does not wish to overwrite existsing file. Return from function
            else:#User entered an invalid response. Ask again.
                print "Invalid response "+response;
    if (verbose):
        print "Restoring file to "+dest;
    shutil.copyfile(os.path.join(archiveDir, 'objects', fileHash), dest);
