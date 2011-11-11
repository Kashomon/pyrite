#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import re
import sys

from .data_structures import blog
        
def buildParser(parse_type): 
    return Parser(parse_type)

class Parser: 
    def __init__(self, parse_type):
        self.blog_parser = blog.BlogParser(parse_type)
        self.parse = self.toplevel_parser(parse_type)

    def toplevel_parser(self, parse_type):
        if parse_type == "yaml":
            return self.parse_yaml
        else:
            print("Unknown file type")
            sys.exit();

    #######################################
    # Below are the type-specific parsers #
    #######################################
    def parse_yaml(self, yaml_str):
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
        return self.blog_parser.parse(postlist_raw) 

    def parse_markdown(self, md_str):
        pass

    def parse_html(self, html_str):
        """
        Takes HTML as string and returns a Post object

        General expectation for HTML: TODO 
        """ 
        pass 

