# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

def parse(string):
    # TODO(josh): Lots of meaty stuff to go here
    return Content(string)

class Content(PostProperty):
    def __init__(self, postbody):
        """
        Constructor should only be accessed by parse method.
        """
        PostProperty.__init__(self, "content")   
        self.postbody = postbody

    def compile(self): 
        return PostProperty.compile(self,self.postbody)

