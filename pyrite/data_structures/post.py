#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import creator
import content

def parse(props_raw, content_raw): 
    post_properties = {}
    for name, value in props_raw.iteritems():
        post_properties[name] = creator.createProperty(name, value)
    content_parsed = content.parse(content_raw)
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

    def addTags(self, tags):
        self.tags = tags
 
    def generate(self):
        ordering = ["title", "date", "tags"]
        compiled = ""
        for prop in ordering:
            if prop in self.post_props:
                compiled += self.post_props[prop].generate()
        compiled += self.post_content.generate()
        return compiled

    def get_date(self):
        return self.post_props["date"]

    def get_title(self):
        return self.post_props["title"]

    def get_filename(self):
        return self.get_date().to_string() + "-" + self.get_title().to_string()

