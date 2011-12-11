# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

import properties 

class ContentParser(object):
  def __init__(self, parse_type, options):
    self.parse_type = parse_type
    self.options = options
    self.css_class = options.CONTENT_CLASS

  def parse(self, string):
    return Content(string.strip(), self.css_class)

class Content(object):
  def __init__(self, post_content, css_class):
    """
    Constructor should only be accessed by the Parser.
    """
    self.post_content = post_content 
    self.css_class = css_class

  def render(self): 
    return properties.generate_html(self.css_class, self.post_content)

  def display_ast(self, indents):
    indenting = indents * "  "
    return (indenting + "Content:" +
      self.post_content.replace("\n", "\n" + indenting) + "\n")


