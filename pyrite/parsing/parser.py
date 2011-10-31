#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import re
import sys
import parsers 
        
def parse(string, parse_type):
    """
    Parse the contents of a file.  The parse_type is determined. 

    Returns: A Blog object 
    """
    parse = parsers.get(parse_type)
    return parse(string)
