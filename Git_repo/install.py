#!/usr/bin/python

import os

var=raw_input("Enter os name:")
print "os name entered is :",var

if var == 'ubuntu':
  os.system("sudo apt-get install mysql-server")
  print "current os ubuntu"
else:
  print "incorrect os"

