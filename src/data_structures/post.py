#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import properties
import content
import random 
import hashlib 

class PostParser(object): 
    def __init__(self, parse_type, options):
        self.parse_type = parse_type
        self.options = options
        self.css_class = options.POST_CLASS
        self.content_parser = content.ContentParser(parse_type, options)
        self.properties_parser = properties.PropertiesParser(
            parse_type, options)

    def parse(self, props_raw, content_raw): 
        post_properties = {}
        if 'date' not in props_raw:
            raise Exception('Parsing Error: Each post must have a date\n' +
                'Props: ' + str(props_raw) + '\n' +
                'Content: ' + str(content_raw)
            )
        for name, value in props_raw.iteritems():
            post_properties[name] = self.properties_parser.parse(name, value)
        content_parsed = self.content_parser.parse(content_raw)
        return Post(post_properties, content_parsed, self.css_class)

         
class Post(object):
    """
    Accepts a number of PostProperties and transforms them to HTML.
    
    param post_properties: dict of post_property objects
    param content: a content object

    """
    def __init__(self, props, post_content, css_class):
        """
        Constructor should only be accessed by parse method.
        """
        self.props = props
        self.post_content = post_content
        self.css_class = css_class
        self.post_id = self._create_id()
 
    def generate(self):
        ordering = ['title', 'date', 'tags']
        compiled = ''
        for key in ordering:
            if key in self.props:
                compiled += self.props[key].generate()
        return properties.generate_html(self.css_class, 
            compiled + self.post_content.generate())

    def get_datetime(self):
        return self.props['date'].date

    def _create_id(self):
        datestr = self.props['date'].to_string() 
        if 'title' in self.props:
            return datestr + "-" + self.props['title'].to_string()
        else:
            return (datestr + "-" +
                hashlib.sha1(self.post_content.generate()).hexdigest()[:12])

    def display_ast(self, indents):
        out = indents * "  " + "Post: " + self.post_id + "\n"
        for propname, propvalue in self.props.iteritems():
            if propvalue is not None and propvalue.display_ast is not None:  
                out += propvalue.display_ast(indents + 1)
        return out + self.post_content.display_ast(indents + 1) + "\n"
