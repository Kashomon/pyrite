#!/usr/bin/python
# Copyright (c) 2011 Joshua Hoak, Alissa Pajer
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import os 

###########
# Reading #
###########

def read_file(name):
    infile = open(name, "r")
    contents = infile.read()
    infile.close()
    return contents


def read_files(path):  
    dir_list = os.listdir(path)
    out = [] 
    for fname in dir_list:
        if file_is_blog_type(fname):
            out.append(read_file(os.path.join(path,fname)))
    return out

######################
# Writing / Creating #
######################

def makedirs_quiet(path):
    print "Making the following path: " + path
    try: 
        os.makedirs(path)
    except IOError as (errno, strerror):
        print "Couldn't make the dirs!"


def write_file(location, contents):  
    outf = open(location, "w")  
    outf.write(contents)
    outf.close()


def write(directory, name, extension, contents):  
    write_file(directory + "/" + name + "." + extension, contents)

############
# Deleting #
############

def clear_blog_gen_files(path):
    to_remove = "html"
    ignore = frozenset('index.html', 'bloglist.html')
    dir_list = os.listdir(path)

def clear_init_files(path):
    to_remove = "html"
    ignore = frozenset("index.html")
    path = std_path(path)
    dir_list = os.listdir(path)

#####################
# Utility Functions #
#####################

def file_is_blog_type(fname):
    available_types = ["yaml"]
    for t in available_types:
        if fname.endswith(t):
            return True
    return False

