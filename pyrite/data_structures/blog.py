#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import date_prop
import json
import post 
import os 

from .. import file_util 
from .. import psettings
from .. import templater
from ..util import safe_get

from mako.template import Template

POST_TEMPLATE_DIR = os.path.join(psettings.RES_DIR, psettings.HTML)

class BlogParser(object):
  def __init__(self, parse_type, options):
    self.post_parser = post.PostParser(parse_type, options) 
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

class Blog(object): 
  """ 
  Contains a number of Posts (List of Post)

  Note there should 
  """
  def __init__(self, posts, options):
    self.options = options
    self.posts = posts
    self.title = options.BLOG_NAME
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
    if "tags" in post.props:
      tags_dict = safe_get(self.links, "tags", {})

      for tag in post.props['tags'].tags:
        safe_get(tags_dict, tag, [])
        tags_dict[tag].append(post.post_id)

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
    date_dict[datetuple[0]][month].append(post.post_id)

  def _bin_posts(self, order, post):
    pbin = order / 10 
    if pbin >= 0 and pbin < 10:
      ordd = safe_get(self.links, "ordered_posts", {})
      numbin = safe_get(ordd, pbin, [])
      numbin.append(post.post_id)
    elif pbin < 0: 
      raise Exception("Bin can't be less than zero")
    return 

  def generate_json(self):
    post_path = os.path.join(file_util.get_module_dir(), POST_TEMPLATE_DIR) 
    post_temp_str = file_util.read_file(os.path.join(post_path, "post.html"))
    blog_temp_str = file_util.read_file(os.path.join(post_path, "blog.html"))
    compiled_posts = {}
    for post in self.posts:
      template = Template(post_temp_str)
      compiled_posts[post.post_id] = post.render(template)
    self.links["compiled_posts"] = compiled_posts
    self.links["blog_holder"] = templater.render_blog(
        Template(blog_temp_str), self.title, self.options)
    return json.dumps(self.links, indent=2)

  def display_ast(self):
    out = "Blog: " + self.title + "\n"
    out += "Links: " + str(self.links) + "\n"
    for post in self.posts:
      out += post.display_ast(1)
    return out.strip()

