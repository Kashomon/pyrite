#!/usr/bin/python
# Copyright (c) 2011 Joshua Hoak, Alissa Pajer
# Licensed under the MIT License

import file_util 
from parsing import parser 
import sys

def create(fileloc):
    contents = file_util.read_file(fileloc)
    if contents == "":
        print("Couldn't find file %s" % fileloc) 
        sys.exit(2) 
    blog = parser.parse(contents, "yaml")
    print blog.generate() 
     
