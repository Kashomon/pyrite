#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import properties
import content
import random 

class PostParser: 
    def __init__(self, parse_type):
        self.content_parser = content.ContentParser(parse_type)
        self.properties_parser = properties.PropertiesParser(parse_type)

    def parse(self, props_raw, content_raw): 
        post_properties = {}
        for name, value in props_raw.iteritems():
            post_properties[name] = self.properties_parser.parse(name, value)
        content_parsed = self.content_parser.parse(content_raw)
        return Post(post_properties, content_parsed)
         
class Post:
    """
    Accepts a number of PostProperties and transforms them to HTML.
    
    param post_properties: dict of post_property objects
    param content: a content object

    """
    def __init__(self, post_props, post_content):
        """
        Constructor should only be accessed by parse method.
        """
        self.post_props = post_props
        self.post_content = post_content
        self.post_id = self.get_filename() 
 
    def generate(self):
        ordering = ["title", "date", "tags"]
        compiled = ""
        for prop in ordering:
            if prop in self.post_props:
                compiled += self.post_props[prop].generate()
        return compiled + self.post_content.generate()

    def get_date(self):
        return self.post_props["date"]

    def get_title(self):
        return self.post_props["title"]

    def get_filename(self):
        return self.get_date().to_string() + "-" + self.get_title().to_string()

    def display_ast(self, indents):
        out = indents * "  " + "Post: " + self.post_id + "\n"
        for propname, propvalue in self.post_props.iteritems():
            out += propvalue.display_ast(indents + 1)
        return out + self.post_content.display_ast(indents + 1) + "\n"

