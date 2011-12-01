#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import file_util
import os
import sys
import imp
import templater 
import psettings

##################################
# Input-Directory Initialization #
##################################

def init_or_read_opts(input_dir, output_dir, clean_init):
  if not indir_is_initd(input_dir) and not clean_init:
    init_indir_and_options(input_dir)
    print "Finished initializing Pyrite. Have fun Pyriting!" 

  if clean_init:
    clean_dirs(input_dir, output_dir) 
    init_indir_and_options(input_dir)

  options = read_and_import_options(input_dir)
  init_outdir_if_needed(output_dir, options)
  return options


def indir_is_initd(input_dir):
  file_set = frozenset(os.listdir(input_dir))
  if psettings.OPTIONS_NAME not in file_set:
    return False 
  else: 
    return True
     

def init_indir_and_options(input_dir):
  ensure_base_dir_exists(input_dir)
  print '------------------'
  print 'Pyrite Initializer'
  print '------------------'
  options = read_default_options()
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

  print '\nWhere do you want your generated blog-files to be put?'
  output_location = raw_input('[default=%s]: ' % (
      os.path.join(input_dir, 'pyrite_output')))
  if output_location == '': 
    output_location = os.path.join(input_dir, 'pyrite_output')
  options = options.replace('my_out_location', output_location)
  print '------------------'
  print 'Writing your options to %s' % psettings.OPTIONS_NAME
  print '------------------'

  file_util.write_file(os.path.join(
        input_dir, psettings.OPTIONS_NAME), options)

def read_default_options():
  to_read = os.path.join(
      file_util.get_module_dir(),
      psettings.TEMP_DIR,
      psettings.DEFAULT_OPTS)
  return file_util.read_file(to_read)

def read_and_import_options(input_dir):
  options_mod = None
  opts_file = os.path.join(input_dir, psettings.OPTIONS_NAME)
  print "Importing the options file"
  try: 
    options_mod = imp.load_source("options", opts_file)
  except ImportError:
    print "Couldn't import the options file: %s" % opts_file
    sys.exit(2)
  except IOError:
    print "Couldn't find the specified options file: %s" % opts_file
  return options_mod

################################
# Out-Directory Initialization #
################################

def init_outdir_if_needed(out_dir, opts):
  print '------------------'
  print "Checking for output directory initialization"
  print '------------------'
  ensure_base_dir_exists(out_dir)
  make_out_dirs(out_dir)
  
  copy_template_file(out_dir, psettings.BLOG_JS, opts, rdir=psettings.JS_DIR)
  copy_template_file(out_dir, psettings.JQUERY, opts, rdir=psettings.JS_DIR)
  copy_template_file(out_dir, opts.INDEX_FILE, opts, 
                     in_file=psettings.INDEX_TEMP)

  # Right now, copying all the files. Could copy just the one specified.
  mod_dir = file_util.get_module_dir()    
  for css in os.listdir(os.path.join(mod_dir, psettings.TEMP_DIR, 
        psettings.CSS_DIR)):
    copy_template_file(out_dir, css, opts, rdir=psettings.CSS_DIR)


def copy_template_file(out_dir, out_file, opts, in_file=None, rdir=None): 
  in_path, out_path = create_in_out_pair(out_dir, out_file, in_file, rdir)

  if not out_file == psettings.JQUERY:
    fname = in_file or out_file
    rendered = templater.render_base_templates(in_path, fname, opts)
    file_util.write_file(out_path, rendered)
  else:
    file_util.copy_file_safe(in_path, out_path) 


def create_in_out_pair(out_dir, out_file, in_file=None, connect=None):
  read_path = os.path.join(file_util.get_module_dir(), psettings.TEMP_DIR)
  if connect is not None:  
    read_path = os.path.join(read_path, connect)

  if in_file is not None:
    read_path = os.path.join(read_path, in_file)
  else:
    read_path = os.path.join(read_path, out_file)

  out_path = out_dir
  if connect is not None:  
    out_path = os.path.join(out_path, connect)
  out_path = os.path.join(out_path, out_file)

  return (read_path, out_path)


#####################
# Utility Functions #
#####################

def ensure_base_dir_exists(path): 
  if os.path.isdir(path):
    return
  else:
    # print "The directory: %s doesn't exist." % path
    file_util.makedirs_quiet(path)

def make_out_dirs(out_dir):
  for direct in psettings.DIRS:
    file_util.makedirs_quiet(os.path.join(out_dir, direct))

def clean_dirs(input_dir, output_dir): 
  # print 'Cleaning the pyrite-produced files'
  file_util.remove_file(os.path.join(input_dir, psettings.OPTIONS_NAME))
  file_util.remove_file(os.path.join(output_dir, "pyrite_index.html"))
  moddir = file_util.get_module_dir() 
  for d in psettings.DIRS: 
    dir_path = os.path.join(output_dir, d)
    # dirlist = os.path.listdir(
    file_util.remove_all_files(dir_path)
    file_util.remove_dir(dir_path)

