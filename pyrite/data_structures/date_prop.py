# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

from post_properties import PostProperty 

def parse(string):
    parsed_date = None
    try:
        parsed_date = datetime.strptime(string, "%d/%m/%y")
    except err:
        pass

    try:
        parsed_date = datetime.strptime(string, "%d/%m/%y %H:%M")
    except err
        pass

    if parsed_date == None:
        raise Exception("Unknown date format: " + string)
    else:
        return Date(String)

class Date(PostProperty):   
    """
    The Date Property stores a Date object locally until it comes time to
    create the HTML post, in which case it renders as a String 
    """
    def __init__(self, date):
        """
        Constructor should be accessed by parse method.
        """
        PostProperty.__init__(self, "post_date")    
        self.date = date

    def compile(self):    
        return PostProperty.compile(self, str(self.date))
