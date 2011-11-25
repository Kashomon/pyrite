#!/usr/bin/python
# Copyright (c) 2011 Joshua Hoak, Alissa Pajer
# Licensed under the MIT License

import initr
from parsing import parser 

import file_util 
import sys
import os 

def create(arg_hash):
    # Read in the raw strings from the contents of the files. 
    input_dir = arg_hash['in_dir']
    out_dir = arg_hash['out_dir']

    if arg_hash['clean']: 
        initr.clean_dirs(input_dir, out_dir) 
        sys.exit(1) 

    options = initr.init_or_read_opts(input_dir, out_dir,
        arg_hash['clean_init'])

    raw_contents = []
    if os.path.isdir(input_dir):
        raw_contents = file_util.read_files(input_dir) 
    else:
        raw_contents = [ file_util.read_file(input_dir) ]

    if raw_contents == []:
        raise Exception("Couldn't find file(s): %s" % input_dir) 

    # Build the blog parser so we can parse the raw strings
    blog_parser = parser.buildParser("yaml", options)

    # Parse the YAML files into a blog object
    blog = blog_parser.parse(raw_contents)

    # Sort the posts by date
    blog.sort_posts()

    # Create the links 
    blog.create_links()

    # Display the AST (for the curious)
    print blog.display_ast()

    # Generate the JSON representation    
    print blog.generate_json()

    # Create the necessary pyrite directories 
    # initr.make_pyrite_dirs(out_dir)

    # Generate the blog files 
    # blog.generate(out_dir) 
