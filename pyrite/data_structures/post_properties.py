# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

from date_prop import Date
from tags_prop import Tags
from title_prop import Title

from datetime import datetime

def createProperty(name, value):
    lname = name.lower()
    if lname == "title":
        return Title.parse(value)
    elif lname == "date": 
        return Date.parse(value)
    elif lname == "tags":
        return Tags.parse(value)
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

