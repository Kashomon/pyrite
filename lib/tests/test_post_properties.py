# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import unittest

from datetime import datetime

from .. import post_property 

class TestPostProperties(unittest.TestCase):

    def test_title_compile(self):
        title = post_property.Title("Title")
        self.assertEqual(title.compile(), "<div class=\"post_title\">\nTitle\n</div>")

    def test_post_body_compile(self):
        postbody = post_property.PostBody("Body")
        self.assertEqual(postbody.compile(), "<div class=\"post_body\">\nBody\n</div>")

    def test_date_compile(self):
        now=datetime.now()
        date = post_property.Date(now)
        self.assertEqual(date.compile(), "<div class=\"post_date\">\n"+str(now)+"\n</div>")
"""
    def test_tags_compile(self):
        tags = post_property.PostBody("Body")
        self.assertEqual(postbody.compile(), "<div class=\"post_body\">\nBody\n</div>")        
"""

if __name__ == '__main__':
    unittest.main()

