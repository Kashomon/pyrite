# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

from datetime import datetime
import properties

class Parser(object):
    def __init__(self, parse_type, css_class):
        self.parse_methods = ["%d/%m/%y", "%d/%m/%y %H:%M", "%d %B %Y"]
        # We cache the most successful parsing method at the head of the list
        self.parse_methods.insert(0, self.parse_methods[0])
        self.css_class = css_class
        self.out_format = "%d %B %Y"

    def parse(self, string):
        parsed_date = self.getDatetime(string)
        if parsed_date == None:
            raise Exception("Unknown date format: " + string)
        else:
            return Date(parsed_date, self.css_class, self.out_format)

    def getDatetime(self, string):  
        parsed_date = None
        index = 0
        while index < len(self.parse_methods):
            method = self.parse_methods[index] 
            try: 
                parsed_date = datetime.strptime(string, method) 
            except: 
                pass 

            if parsed_date != None:
                break

            index += 1

        if index > 0 and parsed_date != None:
            to_cache = self.parse_methods[index]
            self.parse_methods.pop(0)
            self.parse_methods.insert(0, to_cache)
            
        if parsed_date == None:
            raise Exception("Couldn't parse the date_string: %s" % string) 
        return parsed_date


class Date(object):   
    """
    The Date Property stores a Date object locally until it comes time to
    create the HTML post, in which case it renders as a String 
    """
    def __init__(self, date, css_class, out_format):
        """
        Constructor should be accessed by parse method.
        """
        self.css_class = css_class
        self.date = date
        self.out_format = out_format
        self.id_format = "%Y-%m-%d"

    def to_string(self):
        return self.date.strftime(self.id_format)

    def display_ast(self, indents):
        indenting = indents * "  "
        return indenting + "Date:" + self.to_string() + "\n"

    ## Generation Methods ## 
    def render_content(self): 
        return self.date.strftime(self.out_format) 

    def generate(self):    
        return properties.generate_html(
            self.css_class, self.render_content()) 


# Utility Methods 
def num_to_month(num): 
    num_dict = {
        1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June",
        7:"July", 8:"August", 9:"September",10:"October",11:"November",
        12:"December"
        }
    return num_dict.get(num)
