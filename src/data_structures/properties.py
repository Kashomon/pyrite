# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

import date_prop
import tags_prop
import title_prop

class PropertiesParser(object):
    def __init__(self, parse_type):
        self.parser_initrs = { 
            "title" : (title_prop, "pyrite_title"),
            "date" : (date_prop, "pyrite_date"),
            "tags" : (tags_prop, "pyrite_tags") 
        }

        self.parsers = {} 
        css_record = ""

        for name, pair in self.parser_initrs.iteritems(): 
            module, css_class = pair
            self.parsers[name] = module.Parser(parse_type, css_class)
            css_record = name + " = " + css_class + "\n"

        # Before we can start writing the css names, we need to pass in the
        # options. 

    def parse(self, name, value):
        lname = name.lower()
        if lname in self.parsers:  
            return self.parsers[lname].parse(value)
        else:
            print "Unknown property: %s" % name

def generate_html(css_class, content):
    return "<div class=\"" + css_class + "\">" + content + "</div>\n"
