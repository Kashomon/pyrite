#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import default_options 
import file_util
import os
import sys

def init_or_read_opts(input_dir, output_dir, clean_init):
    if not indir_is_initd(input_dir):
        init_indir(input_dir)
        print "Finished initializing Pyrite. Have fun Pyriting!" 
        sys.exit(0) 

    if clean_init:
        init_indir(input_dir)

    print "Checking for output initialization"
    # init_outdir_if_needed(output_dir)


def indir_is_initd(input_dir):
    file_set = frozenset(os.listdir(input_dir))
    if "pyrite_options.py" not in file_set:
        return False 
    else: 
        return True
     

def init_indir(input_dir):
    options = read_options()
    file_util.write_file(
        os.path.join(input_dir, "pyrite_options.py"), options_file)
    #print file_util.read_file(default_options.__file__
    #          .replace('.pyc', '.py'))


def read_options():
    to_read = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "templates",
        "default_options.py")
    return file_util.read_file(to_read)

def init_outdir_if_needed(out_dir):
    pass


def read_options(out_dir):
    pass

def make_in_dirs(in_dir): 
    pass

def make_out_dirs(out_dir):
    file_util.makedirs_quiet(os.path.join(input_dir, "pyrite_css"))
    file_util.makedirs_quiet(os.path.join(input_dir, "pyrite_js"))
