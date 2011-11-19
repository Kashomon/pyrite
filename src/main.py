#!/usr/bin/python
# Copyright (c) 2011 Joshua Hoak, Alissa Pajer
# Licensed under the MIT License

import creator 

# Argparse is the right way to do things
import argparse 
import os
import sys
import getopt

def main(argv=None):
    
    """
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
        opts, args = getopt.getopt(sys.argv[1:], "ohinc", ["help", "test",
            "stress", "init"])
    except getopt.GetoptError, err:
        displayHelp()
        print str(err)
        sys.exit(2)

    arg_hash = { 
        'in_dir': os.getcwd(),
        'out_dir': os.path.join(os.getcwd(), 'pyrite_blog'),
        'do_init': False,
        'verbosity': 0
    } 

    print arg_hash

    for o, v in opts:
        if o == "-h" or o == "--help":
            display_help()
            sys.exit(1)
        elif o == "--test":
            arg_hash['in_dir'] = "test_files"
            arg_hash['out_dir'] = "test_files/test_blog_dir"
            break
        elif o == "--stress":
            arg_hash['in_dir'] = "stress_files"
            arg_hash['out_dir'] = "stress_files/test_blog_dir"
            break
        elif o == "-o":
            arg_hash['out_dir'] = v
        else:
            assert False, "Unknown option"  + o

    creator.create(arg_hash)

def display_help():
    print "Usage: <dirname> <opts>"

# Execut the main func
if __name__ == "__main__":
    main()
