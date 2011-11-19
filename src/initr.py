#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import default_options 
import file_util
import os
import sys

def init_or_read_opts(input_dir, output_dir):
    if indir_not_initd(input_dir):
        init_indir(input_dir)
        print "Finished initializing Pyrite. Have fun Pyriting!" 
        # sys.exit(0) 

    print "Checking for output initialization"
    # init_outdir_if_needed(output_dir)


def indir_not_initd(input_dir):
    file_set = frozenset(os.listdir(input_dir))
    if ("pyrite_options.py" in file_set and
        "pyrite_css" in file_set and 
        "pyrite_js" in file_set):
        return False
    else: 
        return True 
     

def init_indir(input_dir):
    if not os.path.exists(os.path.join(input_dir, "pyrite_options.py")):
        options_file = file_util.read_file(
            __file__.replace('initr.py', 'default_options.py'))
        file_util.write_file(
            os.path.join(input_dir, "pyrite_options.py"), options_file)
    #print file_util.read_file(default_options.__file__
    #          .replace('.pyc', '.py'))


def init_outdir_if_needed(out_dir):
    pass


def read_options(out_dir):
    pass

def make_in_dirs(in_dir): 
    pass

def make_out_dirs(out_dir):
    file_util.makedirs_quiet(os.path.join(input_dir, "pyrite_css"))
    file_util.makedirs_quiet(os.path.join(input_dir, "pyrite_js"))
