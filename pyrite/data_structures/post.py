#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)


class Posts: 
    """ 
    Contains a number of Posts 
    """
    def __init__(self, posts):
        self.posts = posts

    # It's not quite clear how compilation should work for Posts
    def compile(self): 
        pass
    

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
