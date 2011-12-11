# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

import properties 

class Parser(object):
  def __init__(self, parse_type, options):
    self.parse_type = parse_type
    self.options = options
    self.css_class = options.TITLE_CLASS

  def parse(self, string): 
    return Title(string.strip(), self.css_class)

class Title(object):
  def __init__(self, title, css_class):
    """
    Constructor should be only accessed by parse method.
    """
    self.css_class = css_class
    self.title = title

  def to_string(self):
    return self.title

  def display_ast(self, indents):
    indenting = indents * "  "
    return indenting + "Title:" + self.to_string() + "\n"

  def render(self): 
    return properties.generate_html(self.css_class, self.title)
