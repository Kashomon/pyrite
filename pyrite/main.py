#!/usr/bin/python
# Copyright (c) 2011 Joshua Hoak, Alissa Pajer
# Licensed under the MIT License

import sys
import creator 
import getopt

def main(argv=None):
    default_loc = None
    out_dir = "blog"
    try:
        opts, args = getopt.getopt(sys.argv[1:], "oh", ["help", "test"])
    except getopt.GetoptError, err:
        displayHelp()
        print str(err)
        sys.exit(2)
    for o, v in opts:
        if o == "-h" or o == "--help":
            displayHelp()
        elif o == "--test":
            default_loc = "test_files/"
            out_dir = "test_files/test_blog_dir"
        elif o == "-o":
            out_dir = v
        else:
            assert False, "Unknown option"  + o

    if len(args) == 0 and default_loc == None:
        displayHelp()
        sys.exit(1)

    if default_loc != None:
        creator.create(default_loc, out_dir)
    else: 
        creator.create(args[0], out_dir)

def displayHelp():
    print "Usage: <dirname> <opts>"

# Execut the main func
if __name__ == "__main__":
    main()
