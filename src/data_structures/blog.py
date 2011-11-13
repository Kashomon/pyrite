#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

# Note: the Blog class was called Posts

import post 
import date_prop
from file_util import write

class BlogParser:
    def __init__(self, parse_type):
        self.post_parser = post.PostParser(parse_type) 

    def parse(self, raw_posts):
        """
        Expects an array of tuples of properties and content and returns as
        parsed blog.
        """
        posts = []
        for props_raw, content_raw in raw_posts:
            posts.append(self.post_parser.parse(props_raw, content_raw))
        return Blog(posts)

class Blog: 
    """ 
    Contains a number of Posts (List of Post)

    Note there should 
    """
    def __init__(self, posts):
        self.posts = posts
        self.title = "BlogoTest"
        self.links = {}

    def sort_posts(self):
        self.posts.sort(key = lambda post: post.get_datetime().timetuple())
        self.posts.reverse()

    def create_links(self):
        for post in self.posts:

            # Create tagging-links
            if "tags" in post.post_props:
                if "tags" not in self.links:
                    self.links["tags"] = {}
                tags_dict = self.links["tags"]

                for tag in post.get_tags():
                    if tag not in tags_dict:
                        tags_dict[tag] = []
                    tags_dict[tag].append(post.get_id())

            # Create date-links
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

    def generate(self, location=None): 
        compiled_posts = [] 
        for post in self.posts:
            compiled_posts.append((post.get_filename(), post.generate()))
        if location != None:
            for fname, content in compiled_posts:
                write(location, fname, "html", content)
        return compiled_posts 

    def display_ast(self):
        out = "Blog: " + self.title + "\n"
        out += "Links: " + str(self.links) + "\n"
        for post in self.posts:
            out += post.display_ast(1)
        return out.strip()
