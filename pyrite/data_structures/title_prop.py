# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

from post_properties import PostProperty

class Title(PostProperty):
    @staticmethod
    def parse(string): 
        return Title(string)

    def __init__(self, title):
        """
        Constructor should be only accessed by parse method.
        """
        PostProperty.__init__(self, "post_title") 
        self.title = title

    def compile(self):    # self.divId is the name of the HTML class
        return PostProperty.compile(self, self.title)
