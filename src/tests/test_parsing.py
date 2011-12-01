# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import unittest

from .. import parser 

yaml_ex = """
---
title: First Post!
date: 1/1/2011 
---
This is my first post!
"""

class TestYamlParsing(unittest.TestCase):

  def test_marked_capture(self):
    self.assertTrue(parser.parse_yaml(yaml_ex)["title"] == "First Post!")

if __name__ == '__main__':
  unittest.main()

