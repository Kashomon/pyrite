# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

from post_property import PostProperty

class ContentParser:
    def __init__(self, parse_type):
        pass

    def parse(self, string):
        # TODO(josh): Lots of meaty stuff to go here
        return Content(string.strip())

class Content(PostProperty):
    def __init__(self, post_content):
        """
        Constructor should only be accessed by parse method.
        """
        PostProperty.__init__(self, "content")   
        self.post_content = post_content 

    def generate(self): 
        return PostProperty.generate(self,self.post_content)

    def display_ast(self, indents):
        indenting = indents * "  "
        return (indenting + "Content:" +
                self.post_content.replace("\n", "\n" + indenting) + "\n")


         

