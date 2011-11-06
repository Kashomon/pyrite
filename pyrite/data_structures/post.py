#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import post_properties 
import content 

def parse(props_raw, content_raw): 
    post_properties = {}
    for name, value in props_raw:
        post_properties[name] = post_properties.createProperty(name, value)
    content = Content.parse(content_raw)
    return Post(post_properties, content)
         
class Post:
    """
    Accepts a number of PostProperties and transforms them to HTML.
    
    param post_properties: dict of post_property objects
    param content: a content object

    """
    def __init__(self, post_properties, content):
        """
        Constructor should only be accessed by parse method.
        """
        self.post_properties = post_properties
        self.content = content

    def addTags(self, tags):
        self.tags = tags
 
    def compile(self):
        compiled = ""
        for name, prop in post_props:
            compiled += prop.compile()
        compiled += content.compile()
        return compiled

    def getDate(self):
        return self.post_properties["date"]
