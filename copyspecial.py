#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
  splPaths=[]
  allPaths=os.listdir(dir)
  for eachPath in allPaths:
#	print "All: ",eachPath
	match=re.search(r'(.*?__[\w]+__.*?\.[\w]{3})', eachPath)
	if match:
#		print "Valid: ",match.group(1)
		absPath=os.path.abspath(match.group(1))
		splPaths.append(absPath)	
  for spl in splPaths:
	print spl
  return splPaths
	
def copy_to(paths, dir):
  for file in paths:
	shutil.copy(file, dir)
  return

def zip_to(paths, zippath):
  paths.insert(0,"zip -j "+zippath)
  cmd=""
  for filePath in paths:
	cmd+=filePath
	cmd+=" " #space between each file name
  print cmd
  (status, output) = commands.getstatusoutput(cmd)
  if(status!=0):
	print "Failed to zip files: "
	print output
  return



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  paths=[]
  for arg in args:
	paths=get_special_paths(arg)
	copy_to(paths, todir)	# get the path of dir
	zip_to(paths, tozip)	# May need to get the path of zippath
	 
if __name__ == "__main__":
  main()
