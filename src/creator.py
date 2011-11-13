#!/usr/bin/python
# Copyright (c) 2011 Joshua Hoak, Alissa Pajer
# Licensed under the MIT License

import file_util 
import sys
import os 

from parsing import parser 

def create(input_dir, out_dir):
    contents = []
    if os.path.isdir(input_dir):
        contents = file_util.read_files(input_dir) 
    else:
        contents = [ file_util.read_file(input_dir) ]

    if contents == []:
        raise Exception("Couldn't find file(s): %s" % input_dir) 

    blog_parser = parser.buildParser("yaml")
    blog = blog_parser.parse(contents)
    print blog.display_ast()

    # The generation phase 
    #make_pyrite_dirs(out_dir)
    #blog.generate(out_dir) 

def make_pyrite_dirs(root_dir):
    to_create = root_dir.rstrip("/")
    makedirs_quiet(to_create + "/css")
    makedirs_quiet(to_create + "/js")
     
def makedirs_quiet(path):
    try: 
        os.makedirs(path)
    except:
        pass
