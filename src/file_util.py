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
  # print "Trying to make the following path: " + path
  try: 
    os.makedirs(path)
    # print "Successful!"
  except OSError as (errno, strerror):
    pass
    # print "Couldn't make the dirs in the path: %s" % path


def write_file(location, contents):  
  outf = open(location, "w")  
  outf.write(contents)
  outf.close()


###########
# Copying #
###########

def copy_file(from_loc, to_loc):
  if os.path.isfile(from_loc):
    write_file(to_loc, read_file(from_loc))

def copy_file_safe(from_loc, to_loc):
  if os.path.isfile(from_loc) and not os.path.isfile(to_loc):
    write_file(to_loc, read_file(from_loc))


############
# Deleting #
############

def remove_all_files(path):
  # print 'attempting to remove all files from %s' % path
  if os.path.isdir(path):
    dir_list = os.listdir(path)
    for file in dir_list:
      to_remove = os.path.join(path, file)
      # print 'removing file: %s' % to_remove
      remove_file(to_remove)
  else: 
    pass

def remove_file(path):
  if os.path.isfile(path):
    # print 'Removing: %s' % path
    os.remove(path)
  else: 
    pass

def remove_dir(path):
  if os.path.exists(path) and os.path.isdir(path):
    if len(os.listdir(path)) != 0:
      pass
      # print "Can't remove dir: %s; not empty" % path
  else:
    # print "Removing dir: %s" % path
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
