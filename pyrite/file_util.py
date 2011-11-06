#!/usr/bin/python
# Copyright (c) 2011 Joshua Hoak, Alissa Pajer
# Licensed under the MIT License 

import os 

def check_okdir(path):
    return os.access(path, os.R_OK)

def read_file(name):
    infile = open(name, "r")
    contents = infile.read()
    infile.close()
    return contents

def read_files(path):  
    dir_list = os.listdir(path)
    for fname in dir_list:
        print fname

def write_file(location, contents):  
    outf = open(location, "w")  
    outf.write(contents)
    outf.close()

def write(directory, name, extension, contents):  
    write_file(directory + "/" + name + "." + extension, contents)
