#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Aaron Deich, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

class Post:
    """
    Accepts a number of PostProperties and transforms them to HTML.
    """
    def __init__(self, title, post, date):
        self.post_properties = {
            "title": title,
            "post" : post,
            "date" : date,
        }

    def addTags(self, tags):
        self.tags = tags
 
    def compile(self):
        compiled = ""
        for name, prop in post_properties:
            compiled += prop.compile()
        return compiled

    def getDate(self):
        return self.post_properties["date"]
