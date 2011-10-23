#!/usr/bin/python
# Copyright (c) 2011 Joshua Hoak, Alissa Pajer
# Licensed under the MIT License 

import os 

def check_okdir(path):
    return os.access(path, os.R_OK)

def read_file(location, name):
    infile = open(location + name, "r")
    contents = infile.read()
    infile.close()
    return contents

def read_files(path):  
    dir_list = os.listdir(path)
    for fname in dir_list:
        print fname

def write_file(location, name, contents):  
    outf = open(location + name, "w")  
    outf.write(contents)
    outf.close()

