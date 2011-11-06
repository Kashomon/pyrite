#!/usr/bin/python
# Copyright (c) 2011 Joshua Hoak, Alissa Pajer
# Licensed under the MIT License

import sys
import creator 
import getopt

def main(argv=None):
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help", "test"])
    except getopt.GetoptError, err:
        displayHelp()
        print str(err)
        sys.exit(2)
    for o, a in opts:
        if o == "-h":
            displayHelp()
        if o == "--test":
            creator.create("test_files/testblog.yaml")
            sys.exit(1)
        else:
            assert False, "Unknown option"  + o

    if len(args) == 0:
        displayHelp()
        sys.exit(1)

    creator.create(args[0])

def displayHelp():
    print "Usage: <dirname> <opts>"

# Execut the main func
if __name__ == "__main__":
    main()
