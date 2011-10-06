# Copyright (c) 2011 by Joshua Hoak, Aaron Deich, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

#TODO (josh): Perhaps properties should be in charge of their own parsing? 
#TODO (josh): Perhaps each class should be its own file?

from datetime import datetime

class PostProperty:
    """
    Defines a property of a post.  All properties get their own div class and
    get rendered as HTML.
    """
    def __init__(self, divId):  
        self.divId = divId  

    def compile(self, content):
        return "<div class=\"" + self.divId + "\">\n" +  content + "\n</div>\n"


class Title(PostProperty):
    def __init__(self, title):
        PostProperty.__init__(self, "post_title")     # "post_title" is the HTML class of Title
        self.title = title

    def compile(self):    # self.divId is the name of the HTML class
        return PostProperty.compile(self, self.title)

class PostBody(PostProperty):
    def __init__(self, postbody):
        PostProperty.__init__(self, "post_body")    # "post_body" is the HTML class of PostBody
        self.postbody = postbody

    def compile(self): 
        return PostProperty.compile(self,self.postbody)

class Date(PostProperty):    # the instance of Date which returns the current datetime is Date(now)
    """
    The Date Property stores a Date object locally until it comes time to
    create the HTML post, in which case it renders as a String 
    """
    def __init__(self, date):
        PostProperty.__init__(self, "post_date")    # "post_date" is the HTML class of PostBody
        self.date = date

    def compile(self):    
        return PostProperty.compile(self, str(self.date))

class Tags(PostProperty):
    """
    Stores a list of topic-tags
    """
    def __init__(self, tags):
        PostProperty.__init__(self, "post_tags")    # "post_tags" is the HTML class of Tags
        self.tags = tags

    def compile(self):
        output = ""
        for item in self.tags:
          output += PostProperty.compile(self, item)
        return output


#print PostProperty.compile(PostProperty("class_goes_here"),"Content goes here.")
#
#print Title.compile(Title("Content of Title goes here."))
#
#print PostBody.compile(PostBody("Content of post goes here."))
#
#print Date.compile(Date(datetime.now()))
#
#print Tags.compile(Tags(["tag1", "tag2", "tag3"]))
#
