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
    print "Trying to make the following path: " + path
    try: 
        os.makedirs(path)
        print "Successful!"
    except IOError as (errno, strerror):
        print "Couldn't make the dirs in the path: %s" % path


def write_file(location, contents):  
    outf = open(location, "w")  
    outf.write(contents)
    outf.close()


############
# Deleting #
############

def remove_all_files(path):
    if os.path.exists(path) and os.path.isdir(path):
        dir_list = os.listdir(path)
        for file in dir_list:
            remove_file(os.path.join(file))

def remove_file(path):
    if os.path.isfile(path):
        print 'Removing: %s' % path
        os.remove(path)

def remove_dir(path):
    if os.path.exists(path) and os.path.isdir(path):
        if len(os.listdir(path)) != 0:
            print "Can't remove dir: %s; not empty" % path
        else:
            print "Removing dir: %s" % path
            os.rmdir(path)

#####################
# Utility Functions #
#####################

def file_is_blog_type(fname):
    available_types = ["yaml"]
    for t in available_types:
        if fname.endswith(t):
            return True
    return False

def get_module_dir(): 
    return os.path.dirname(os.path.realpath(__file__))
