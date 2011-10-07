#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import re
        
def parse_yaml(yaml_str):
    """
    Parse a YAML post and return a Post object
    ---
    title: Post
    tags: code, fun, python
    date: 2 August 2011, 2:00p GMT 
    ... / more tags / ...
    ---
    Blog post content
    """
    out = {} 
    sections =  yaml_str.split("---")
    out["content"] = sections[2].strip()
    for line in sections[1].split("\n"):
        tag, splitter, data = line.partition(":")
        out[tag.strip()] = data.strip()
    return out 


def parse_markdown(mk_str):
    pass

def parse_html(html_str):
    """
    Takes HTML as string and returns a Post object

    General expectation for HTML: TODO 
    """ 
    pass 

