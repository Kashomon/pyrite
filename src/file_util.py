#!/usr/bin/python
# Copyright (c) 2011 Joshua Hoak, Alissa Pajer
# Licensed under the MIT License 

import os 

def fileIsBlogType(fname):
    available_types = ["yaml"]
    for t in available_types:
        if fname.endswith(t):
            return True
    return False

def check_okdir(path):
    return os.access(path, os.R_OK)

def read_file(name):
    infile = open(name, "r")
    contents = infile.read()
    infile.close()
    return contents

def read_files(path):  
    if not path.endswith("/"):
        path = path + "/"
    dir_list = os.listdir(path)
    out = [] 
    for fname in dir_list:
        if fileIsBlogType(fname):
            out.append(read_file(path + fname))
    return out

def write_file(location, contents):  
    outf = open(location, "w")  
    outf.write(contents)
    outf.close()

def write(directory, name, extension, contents):  
    write_file(directory + "/" + name + "." + extension, contents)

