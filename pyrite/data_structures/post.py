#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import post_properties 
from content import Content 

class Posts: 
    """ 
    Contains a number of Posts (List of Post)

    Note there should 
    """
    def __init__(self, posts):
        self.posts = posts

    def compile(self): 
        for post in self.posts:
            # write to disk 
            pass
         
class Post:
    """
    Accepts a number of PostProperties and transforms them to HTML.
    
    param post_properties: dict of post_property objects
    param content: a content object

    """
    @staticmethod
    def parse(props_raw, content_raw): 
        post_properties = {}
        for name, value in props_raw:
            post_properties[name] = post_properties.createProperty(name, value)
        content = Content.parse(content_raw)
        return Post(post_properties, content)

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
