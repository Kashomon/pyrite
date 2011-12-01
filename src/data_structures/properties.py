# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

import date_prop
import tags_prop
import title_prop

class PropertiesParser(object):
  def __init__(self, parse_type, options):
    self.options = options
    self.parsers = { 
        "title" : title_prop.Parser(parse_type, options),
        "date" : date_prop.Parser(parse_type, options),
        "tags" : tags_prop.Parser(parse_type, options)
    }

  def parse(self, name, value):
    lname = name.lower()
    if lname in self.parsers:  
      return self.parsers[lname].parse(value)
    else:
      print "Unknown property: %s" % name

def generate_html(css_class, content):
  return "<div class=\"" + css_class + "\">" + content + "</div>\n"
