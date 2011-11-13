#!/usr/bin/python
# Copyright (c) 2011 Joshua Hoak, Alissa Pajer
# Licensed under the MIT License

import file_util 
import sys
import os 

from parsing import parser 

def create(input_dir, out_dir):
    contents = []

    # Read in the raw strings from the contents of the files. 
    if os.path.isdir(input_dir):
        contents = file_util.read_files(input_dir) 
    else:
        contents = [ file_util.read_file(input_dir) ]

    if contents == []:
        raise Exception("Couldn't find file(s): %s" % input_dir) 

    # Build the blog parser so we can parse the raw strings
    blog_parser = parser.buildParser("yaml")

    # Parse the YAML files into a blog object
    blog = blog_parser.parse(contents)

    # Sort the posts by date
    blog.sort_posts()

    # Create the links 
    blog.create_links()

    #print blog.display_ast()

    # Create the necessary pyrite directories 
    make_pyrite_dirs(out_dir)

    # Generate the blog files 
    blog.generate(out_dir) 

def make_pyrite_dirs(root_dir):
    to_create = root_dir.rstrip("/")
    makedirs_quiet(to_create + "/css")
    makedirs_quiet(to_create + "/js")

def clear():
    pass
     
def makedirs_quiet(path):
    try: 
        os.makedirs(path)
    except:
        pass
