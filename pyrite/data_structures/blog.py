#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 

# Author: Josh Hoak (jrhoak@gmail.com)
# Note: the Blog class was called Posts

import post 
from file_util import write

def parse(raw_posts):
    posts = []
    for props_raw, content_raw in raw_posts:
        posts.append(post.parse(props_raw, content_raw))
    return Blog(posts)

class Blog: 
    """ 
    Contains a number of Posts (List of Post)

    Note there should 
    """
    def __init__(self, posts):
        self.posts = posts

    def generate(self, location=None): 
        compiled_posts = [] 
        for post in self.posts:
            compiled_posts.append( (post.get_filename(), post.generate()) )
        if location != None:
            for fname, content in compiled_posts:
                write(location, fname, "html", content)
        return compiled_posts 


