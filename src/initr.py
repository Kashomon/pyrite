#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import file_util

def indir_not_initd(input_dir):
    pass

def init_indir(input_dir):
    pass

def init_outdir_if_needed(out_dir):
    pass

def read_options(out_dir):
    pass

def make_pyrite_dirs(out_dir):
    file_util.makedirs_quiet(os.path.join(root_dir, "css"))
    file_util.makedirs_quiet(os.path.join(to_create, "js"))
