# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

import date_prop
import tags_prop
import title_prop

from datetime import datetime

def createProperty(name, value):
    lname = name.lower()
    if lname == "title":
        return title_prop.parse(value)
    elif lname == "date": 
        return date_prop.parse(value)
    elif lname == "tags":
        return tags_prop.parse(value)
    else:
        raise Exception("Unknown property: %s" % name)

class PostProperty:
    """
    Defines a property of a post: a sort of abstract class.   All properties
    get their own div class and get rendered as HTML.
    """
    def __init__(self, divId):  
        self.divId = divId  

    def compile(self, content):
        return "<div class=\"" + self.divId + "\">\n" +  content + "\n</div>\n"

