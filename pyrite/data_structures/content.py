# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

from post_property import PostProperty

class ContentParser:
    def __init__(self, parse_type):
        pass

    def parse(self, string):
        # TODO(josh): Lots of meaty stuff to go here
        return Content(string)

class Content(PostProperty):
    def __init__(self, postbody):
        """
        Constructor should only be accessed by parse method.
        """
        PostProperty.__init__(self, "content")   
        self.postbody = postbody

    def generate(self): 
        return PostProperty.generate(self,self.postbody)

