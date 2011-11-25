#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

from templates import default_options 
import file_util
import os
import sys

OPTIONS_NAME = "pyrite_options.py"
CSS_DIR = "pyrite_css" 
JS_DIR = "pyrite_js" 
MEDIA_DIR = "pyrite_media"

DIRS = [CSS_DIR, JS_DIR, MEDIA_DIR]

def init_or_read_opts(input_dir, output_dir, clean_init):
    if not indir_is_initd(input_dir) and not clean_init:
        init_indir(input_dir)
        print "Finished initializing Pyrite. Have fun Pyriting!" 
        sys.exit(0) 

    if clean_init:
        clean_dirs(input_dir, output_dir) 
        init_indir(input_dir)

    init_outdir_if_needed(output_dir)


def indir_is_initd(input_dir):
    file_set = frozenset(os.listdir(input_dir))
    if OPTIONS_NAME not in file_set:
        return False 
    else: 
        return True
     

def init_indir(input_dir):
    check_dir_exists(input_dir)
    print '------------------'
    print 'Pyrite Initializer'
    print '------------------'
    options = read_options()
    print 'Let\'s initialize your blog with some initial settigns'
    print 'You can change them later in the generated pyrite_options.py'
    print ''
    print 'What do you want your blog to be called?'
    blog_name = raw_input('[default=PyriteBlog]: ')
    if blog_name == '': blog_name = 'PyriteBlog'
    print ''
    print 'Your blog will be called: %s' % blog_name
    print '------------------'
    blog_name
    options = options.replace('MyBlogName', blog_name)

    print 'Where do you want your blog-files to be read from?'
    input_location = raw_input('[default=%s]: ' % (input_dir))
    if input_location == '': input_location = input_dir
    options = options.replace('my_in_location', input_location)

    print '' 
    print 'Where do you want your generated blog-files to be put?'
    output_location = raw_input('[default=%s]: ' % (
        os.path.join(input_dir, 'pyrite_output')))
    if output_location == '': output_location = (
        os.path.join(input_dir, 'pyrite_output'))
    options = options.replace('my_out_location', output_location)
    print '------------------'
    print 'Writing your options to %s' % OPTIONS_NAME
    print '------------------'

    file_util.write_file(
        os.path.join(input_dir, OPTIONS_NAME), options)

def read_options():
    to_read = os.path.join(
        file_util.get_module_dir(),
        "templates",
        "default_options.py")
    return file_util.read_file(to_read)


def init_outdir_if_needed(out_dir):
    print '------------------'
    print "Checking for output directory initialization"
    print '------------------'
    check_dir_exists(out_dir)
    make_out_dirs(out_dir)

def check_dir_exists(path): 
   if os.path.isdir(path):
        return
   else:
        print "The directory: %s doesn't exist." % path
        make_base_dirs(path)

def make_base_dirs(path): 
   file_util.makedirs_quiet(path) 


def make_out_dirs(out_dir):
    for direct in DIRS:
        file_util.makedirs_quiet(os.path.join(out_dir, direct))

def clean_dirs(input_dir, output_dir): 
    print 'Cleaning the pyrite-produced files'

    opts = os.path.join(input_dir, OPTIONS_NAME) 
    file_util.remove_file(opts)
    for d in DIRS: 
        dir_path = os.path.join(output_dir, d)
        file_util.remove_all_files(dir_path)
        file_util.remove_dir(dir_path)
