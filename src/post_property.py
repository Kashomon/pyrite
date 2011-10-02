# Copyright (c) 2011 by Joshua Hoak, Aaron Deich, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import datetime 

#TODO (josh): Perhaps properties should be in charge of their own parsing? 
#TODO (josh): Perhaps each class should be its own file?
class PostProperty:
    """
    Defines a property of a post.  All properties get their own divid and
    get rendered as HTML.
    """
    def __init__(self, divId):  
        self.divId = divId  

    def compile(self, content):
        return "<div id = " + self.divId + ">\n" +  content + "\n</div>"


class Title(PostProperty):
    def __init__(self, title):
        PostProperty.__init__(self, "post_title")
        self.title = title

    def compile(self): 
        return PostProperty.compile(self, self.title)

# TODO(josh): these classes need finishing 
class PostBody(PostProperty):
    def __init__(self, post_body):
        pass

    def compile(self):
        pass

class Date(Property):
    """
    The Date Property stores a Date object locally until it comes time to
    create the HTML post, in which case it renders as a String 
    """
    def __init__(self, date):
        pass

    def compile(self):
        pass 

class Tags(Property):
    """
    Stores a list of topic-tags
    """
    def __init__(self, tags):
        pass 

    def compile(self):
        pass 

