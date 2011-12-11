#!/usr/bin/python
# Copyright (c) 2011 Joshua Hoak
# Licensed under the MIT License

import initr
import parser 
import psettings

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
    "Couldn't find any blog file(s) in: %s" % input_dir
    sys.exit(0)

  # Build the blog parser so we can parse the raw strings
  blog_parser = parser.buildParser("yaml", options)

  # Parse the YAML files into a blog object
  blog = blog_parser.parse(raw_contents)

  # Sort the posts by date
  # TODO(josh): Should this be internal to the blog? 
  blog.sort_posts()

  # Create the links 
  blog.create_links()

  # Display the AST (for the curious)
  # print blog.display_ast()

  # Generate the JSON representation    
  json_out = "var pyrite_data = " + (blog.generate_json().strip()) + ";" 
  # print json_out

  # Create the necessary pyrite directories 
  json_path = os.path.join(out_dir, psettings.JS_DIR, psettings.DATA_FILE)
  file_util.write_file(json_path, json_out)
