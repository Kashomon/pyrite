# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

class PostProperty(object):
    """
    Defines a property of a post: a sort of abstract class.   All properties
    get their own div class and get rendered as HTML.
    """
    def __init__(self, divId):  
        self.divId = divId  

    def generate(self, content):
        return "<div class=\"" + self.divId + "\">\n" +  content + "\n</div>\n"

