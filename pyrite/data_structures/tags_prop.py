# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

import properties 

class Parser(object):
  def __init__(self, parse_type, options):
    self.parse_type = parse_type
    self.options = options
    self.css_class = options.TAGS_CLASS

  def parse(self, tags_raw): 
    return Tags(tags_raw.split(","), self.css_class)

class Tags(object):
  """
  Stores a list of topic-tags
  """
  def __init__(self, tags, css_class):
    """
    Constructor should only be accessed by parse method.
    """
    self.tags = tags
    self.css_class = css_class

  def to_string(self):
    return str(self.tags)

  def display_ast(self, indents):
    return (indenting * "  ") + "Tags:" + str(self.tags) + "\n"

  def render(self):
    return properties.generate_html(self.css_class, 
        reduce(lambda x, y: x + "," + y, self.tags))
       
