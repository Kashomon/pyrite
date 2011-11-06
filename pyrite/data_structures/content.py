# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

#TODO (josh): Perhaps properties should be in charge of their own parsing? 
#TODO (josh): Perhaps each class should be its own file?

class Content(PostProperty):
    @staticmethod
    def parse(string):
        # TODO(josh): Lots of meaty stuff to go here
        return Content(string)

    def __init__(self, postbody):
        """
        Constructor should only be accessed by parse method.
        """
        PostProperty.__init__(self, "content")   
        self.postbody = postbody

    def compile(self): 
        return PostProperty.compile(self,self.postbody)

