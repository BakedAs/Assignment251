__author__ = 'FrancisGreatorex'
import os, os.path, hashlib, json;

def createFileSignature (filename):
    """CreateFileHash (file): create a signature for the specified file
       Returns a tuple containing three values:
          (the pathname of the file, its last modification time, SHA1 hash)
    """
    f = None
    signature = None
    try:
        filesize  = os.path.getsize(filename)
        modTime   = int(os.path.getmtime(filename))

        f = open(filename, "rb")  # open for reading in binary mode
        hash = hashlib.sha1()
        s = f.read(16384)
        while (s):
            hash.update(s)
            s = f.read(16384)

        hashValue = hash.hexdigest()
        signature = (filename,  modTime, hashValue)
    except IOError:
        signature = None
    except OSError:
        signature = None
    finally:
        if f:
            f.close()
    return(signature)

#to search for an filename via an index

#Loads the index file from the specified archive directory. Returns a dictionary with file paths as keys and file hashes as values.
def loadIndex (archiveDir):
    indexFile = os.path.join(archiveDir, "index.txt");
    if (not os.path.exists(indexFile)):
        raise IOError("Index not found at "+indexFile);
    return json.load(open(indexFile, "r"));

#Saves the index to the specified archive directory
def saveIndex (archiveDir, index):
    indexFile = os.path.join(archiveDir, "index.txt");
    if (not os.path.exists(indexFile)):
        raise IOError("Index not found at "+indexFile);
    json.dump(index, open(indexFile, "w"),indent=4);
        
