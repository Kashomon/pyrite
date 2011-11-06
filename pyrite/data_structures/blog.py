#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 

# Author: Josh Hoak (jrhoak@gmail.com)
# Note: the Blog class was called Posts

import post 

def parse(raw_posts):
    posts = []
    for props_raw, content_raw in raw_posts:
        posts.add(post.parse(props_raw, content_raw))
    return Blog(posts)

class Blog: 
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
