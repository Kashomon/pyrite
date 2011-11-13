# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

from post_property import PostProperty 

class TagsParser:
    def __init__(self, parse_type):
        pass

    def parse(self, tags_raw): 
        return Tags(tags_raw.split(","))

class Tags(PostProperty):
    """
    Stores a list of topic-tags
    """
    def __init__(self, tags):
        """
        Constructor should only be accessed by parse method.
        """
        PostProperty.__init__(self, "post_tags")
        self.tags = tags

    def generate(self):
        output = ""
        for item in self.tags:
          output += PostProperty.generate(self, item)
        return output

    def display_ast(self, indents):
        indenting = indents * "  "
        return indenting + "Tags:" + str(self.tags) + "\n"
