# Assignment 2 159.251

## **Members:**<br />
Francis - 14136398<br />
Josh - 11264379 <br />

## **About:**<br />

This is a program which can protect your data by saving it into an archive directory.    
The directory has been constructed in such a way as to give every file a unique signature
and only save the same content once, regardless of how many file names with that content exist.
It has been created by two software engineering students at Massey University.

## **Instructions:**<br />
To run the program, download the source and unzip it to the archive directory you wish to backup.
Use a terminal or command line to change to the directory containing the archive e.g: cd /path/to/directory
If you have Python as part of your path: (OSX and Linux have this built in)
    If you are using Windows, download Python 2.X and use 'python' in front of commands for example:

       python mybackup.py init

   1. Run the command: ./mybackup.py init - to initialize the backup folder
   2. The use any of the following commands depending on what you want to do:

       *   ./mybackup.py &lt;command&gt; &lt;parameter&gt;

       Where command is:

       *    store - will backup the directory and subsequent sub-directories given as parameter
       *    restore - will restore the the directory or file given as a parameter
       *    list - will display all of the directories or files given as a parameter or all if no parameter given
       *    get - will get the file specified by the parameter given and restore it into the current working directory
       *    test - will test the validity of the backup ensuring all files are accounted for and the file names match
       the objects created in the objects directory (no parameter required)