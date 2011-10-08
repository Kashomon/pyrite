#!/usr/bin/python
# Copyright (c) 2011 Joshua Hoak, Alissa Pajer
# Licensed under the MIT License

import sys

def main(argv=None):
    if argv is None: argv = sys.argv[1:]
    argdict = process_args(argv)

#TODO(jhoak): Consider using getopt for arg processing 
def process_args(args):
    out = {} 
    if len(args) == 0:
        print "Usage: <dirname> <opts>"
        sys.exit(1)
   
    if len(args) == 1:
        out["path"] = args[0]
    else:
        print("Unfortunately, only have path-processing at the moment")
        sys.exit(1)

# Execut the main func
if __name__ == "__main__":
    main()
