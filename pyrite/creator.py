#!/usr/bin/python
# Copyright (c) 2011 Joshua Hoak, Alissa Pajer
# Licensed under the MIT License

import file_util 
import sys
import os 

from parsing import parser 

def create(fileloc, out_dir):
    contents =""
    if os.path.isdir(fileloc):
        print file_util.read_files(fileloc) 
        sys.exit(0)
    else:
        contents = file_util.read_file(fileloc)

    if contents == "":
        print("Couldn't find file %s" % fileloc) 
        sys.exit(2) 

    blog_parser = parser.buildParser("yaml")
    blog = blog_parser.parse(contents)

    # The generation phase 
    make_pyrite_dirs(out_dir)
    blog.generate(out_dir) 

def make_pyrite_dirs(root_dir):
    to_create = root_dir.rstrip("/")
    makedirs_quiet(to_create + "/css")
    makedirs_quiet(to_create + "/js")
     
def makedirs_quiet(path):
    try: 
        os.makedirs(path)
    except:
        pass
