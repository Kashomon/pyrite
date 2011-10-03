# Copyright (c) 2011 by Joshua Hoak, Aaron Deich, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import unittest

from .. import post_property 

class TestPostProperties(unittest.TestCase):

    def test_title_compile(self):
        title = post_property.Title("Post")
        self.assertEqual(title.compile(), ("<div class=\"post_title\""+
            "\">\nPost\n</div>"))

    def test_post_body_compile(self):
        pass

    def test_date_compile(self):
        pass

    def test_tags_compile(self):
        pass

if __name__ == '__main__':
    unittest.main()


