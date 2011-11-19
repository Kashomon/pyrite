# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

import date_prop
import tags_prop
import title_prop

class PropertiesParser(object):
    def __init__(self, parse_type):
        self.title_parser   = title_prop.TitleParser(parse_type)
        self.date_parser    = date_prop.DateParser(parse_type)
        self.tags_parser    = tags_prop.TagsParser(parse_type)

    def parse(self, name, value):
        lname = name.lower()
        if lname == "title":
            return self.title_parser.parse(value)
        elif lname == "date": 
            return self.date_parser.parse(value)
        elif lname == "tags":
            return self.tags_parser.parse(value)
        else:
            print "Unknown property: %s" % name

