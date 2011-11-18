#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

# Note: the Blog class was called Posts

import post 
import date_prop
from file_util import write
import json

class BlogParser:
    def __init__(self, parse_type, options):
        self.post_parser = post.PostParser(parse_type) 
        self.options = options

    def parse(self, raw_posts):
        """
        Expects an array of tuples of properties and content and returns as
        parsed blog.
        """
        posts = []
        for props_raw, content_raw in raw_posts:
            posts.append(self.post_parser.parse(props_raw, content_raw))
        return Blog(posts, self.options)

class Blog: 
    """ 
    Contains a number of Posts (List of Post)

    Note there should 
    """
    def __init__(self, posts, options):
        self.options = options
        self.posts = posts
        self.title = "BlogoTest"
        self.links = {}

    def sort_posts(self):
        self.posts.sort(key = lambda post: post.get_datetime().timetuple())
        self.posts.reverse()

    def create_links(self):
        order = 0
        for post in self.posts:
            self._create_tagging_links(post)
            self._create_date_links(post)
            self._bin_posts(order, post)
            order += 1

    def _create_tagging_links(self, post):
        if "tags" in post.post_props:
            tags_dict = get_or_else(self.links, "tags", {})

            for tag in post.get_tags():
                get_or_else(tags_dict, tag, [])
                tags_dict[tag].append(post.get_id())

    def _create_date_links(self, post):
        if "dates" not in self.links:
            self.links["dates"] = {}
        
        datetuple = post.get_datetime().timetuple()
        date_dict = self.links["dates"]

        if datetuple[0] not in date_dict:
            date_dict[datetuple[0]] = {} 

        month = date_prop.num_to_month(datetuple[1])
        if month not in date_dict[datetuple[0]]:
            date_dict[datetuple[0]][month] = []
        date_dict[datetuple[0]][month].append(post.get_id())

    def _bin_posts(self, order, post):
        pbin = order / 10 
        if pbin >= 0 and pbin < 10:
            ordd = get_or_else(self.links, "ordered_posts", {})
            numbin = get_or_else(ordd, pbin, [])
            numbin.append(post.get_id())  
        elif pbin < 0: 
            raise Exception("Bin can't be less than zero")
        return 

    def generate(self): 
        compiled_posts = [] 
        for post in self.posts:
            compiled_posts.append((post.get_filename(), post.generate()))
        return compiled_posts 

    def generate_json(self):
        compiled_posts = {}
        for post in self.posts:
            compiled_posts[post.get_id()] = post.generate()
        self.links["compiled_posts"] = compiled_posts
        return json.dumps(self.links, indent=4)

    def display_ast(self):
        out = "Blog: " + self.title + "\n"
        out += "Links: " + str(self.links) + "\n"
        for post in self.posts:
            out += post.display_ast(1)
        return out.strip()

def get_or_else(di, item, df):
    if item not in di:
        di[item] = df
    return di[item]
