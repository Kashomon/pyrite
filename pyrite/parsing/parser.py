#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import re
import sys

from .data_structures import blog
        
def parse(string, parse_type):
    """
    Parse the contents of a file.  The parse_type is determined. 

    Returns: A Blog object 
    """
    parser = get(parse_type)
    return parser(string)

def get(parse_type):
    if parse_type == "yaml":
        return parse_yaml
    else:
        print("Unknown file type")
        sys.exit();

def parse_yaml(yaml_str):
    """
    Parse a YAML post and return a Post object
    ---
    title: Post
    tags: code, fun, python
    date: 2 August 2011, 2:00
    ... / more tags / ...
    ---
    Blog post content
    """
    sections =  yaml_str.split("---")
    content_raw = sections[2].strip()

    tags_raw = {} 
    for line in sections[1].strip().split("\n"):
        tag, splitter, data = line.partition(":")
        tags_raw[tag.strip()] = data.strip()

    postlist_raw = [ (tags_raw, content_raw) ]
    return blog.parse(postlist_raw) 

def parse_markdown(mk_str):
    pass

def parse_html(html_str):
    """
    Takes HTML as string and returns a Post object

    General expectation for HTML: TODO 
    """ 
    pass 

