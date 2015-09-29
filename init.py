__author__ = 'JoshBaker'
import os, os.path

#Define archive location
myArchive = os.path.expanduser("~/myArchive")

if os.path.exists(myArchive) and os.path.isdir(myArchive):
  print "Archive Directory exists"
else:
  print "Archive Directory not yet created"