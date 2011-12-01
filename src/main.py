#!/usr/bin/python
# Copyright (c) 2011 Joshua Hoak, Alissa Pajer
# Licensed under the MIT License

import creator 

# Argparse is the right way to do things
import argparse 
import os
import sys
import getopt
import file_util
import __init__

def main(argv=None):
  
  """
  # This doesn't work yet but it's the right way to do things.
  parser = argparse.ArgumentParser(
          description='Pyrite: A static blog generator!')
  parser.add_argument(
      'In Directory', metavar="F", default=os.getcwd(),
      help=('The input directory. Default is the current working directory'))
  parser.add_argument('--test', help='Run the pyrite test')
  args = parser.parse_args(argv)

  print args
  sys.exit(1)
  """

  try:
    opts, args = getopt.getopt(sys.argv[1:], 'ohincv', ['help', 'test',
        'stress', 'init', 'clean_init', 'clean', 'version'])
  except getopt.GetoptError, err:
    display_help()
    print str(err)
    sys.exit(2)

  arg_hash = { 
      'in_dir': os.getcwd(),
      'out_dir': os.path.join(os.getcwd(), 'pyrite_blog'),
      'clean_init': False,
      'clean': False,
      'verbosity': 0,
  } 

  # print arg_hash

  for o, v in opts:
    if o == '-h' or o == '--help':
      display_help()
      sys.exit(1)
    elif o == '--test':
      arg_hash['in_dir'] = os.path.join( 
          file_util.get_module_dir(), "test_files")
      arg_hash['out_dir'] = os.path.join(
          file_util.get_module_dir(), "test_files", "pyrite_blog")
      arg_hash['clean_init'] = True
    elif o == "--stress":
      arg_hash['in_dir'] = "stress_files"
      arg_hash['out_dir'] = "stress_files/test_blog_dir"
    elif o == "--clean_init":
      arg_hash['clean_init'] = True
    elif o == '-o':
      arg_hash['out_dir'] = v
    elif o == '-c' or o == '--clean':
      arg_hash['clean'] = True
    elif o == '-v' or o == '--version':
      print 'Pyrite Version %s' % __init__.__version__ 
      sys.exit(0)
    else:
      assert False, 'Unknown option'  + o

  creator.create(arg_hash)

def display_help():
  print "Usage: <dirname> <opts>"

# Execut the main func
if __name__ == "__main__":
  main()
