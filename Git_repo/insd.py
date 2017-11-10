#!/usr/bin/python

import os

a=1

if [ a == 0 ]:
  print "Installing httpd on Centos"
  os.system "sudo yum install httpd"
else:
  print "Installing apache2 on Ubuntu os"
  os.system "sudo apt-get install apache2"

