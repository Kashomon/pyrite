# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

from datetime import datetime

from post_property import PostProperty

def parse(string):
    parsed_date = _getDatetime(string)
    if parsed_date == None:
        raise Exception("Unknown date format: " + string)
    else:
        return Date(parsed_date)

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

    def generate(self):    
        return PostProperty.generate(self, self.date.strftime("%Y-%m-%d"))

    def to_string(self):
        return self.date.strftime("%Y-%m-%d")


def _getDatetime(string):  
    parse_methods = ["%d/%m/%y", "%d/%m/%y %H:%M", "%d %B %Y"]
    parsed_date = None
    for method, index in zip(parse_methods, range(len(parse_methods))):
        try: 
            parsed_date = datetime.strptime(string, method) 
        except: 
            pass 

        if parsed_date != None:
            break

    if parsed_date != None:
        parse_methods = parse_methods.insert(0, parse_methods.pop(index))

    return parsed_date

