# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

import date_prop
import tags_prop
import title_prop

def createProperty(name, value):
    lname = name.lower()
    if lname == "title":
        return title_prop.parse(value)
    elif lname == "date": 
        return date_prop.parse(value)
    elif lname == "tags":
        return tags_prop.parse(value)
    else:
        raise Exception("Unknown property: %s" % name)
