#!/usr/bin/python
# Copyright (c) 2011 Joshua Hoak
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import file_util
import psettings
import sys

from mako.template import Template


def simple_render(template, opts):
  return template.render()
    
def render_base_templates(in_path, file, opts): 
  render_methods = { 
    psettings.BLOG_JS : simple_render,
    psettings.INDEX_TEMP : index_render
  }

  if file in render_methods:
    template = Template(filename=in_path)
    return render_methods.get(file)(template, opts)
  else:
    return file_util.read_file(in_path)

def index_render(template, opts):
  return template.render(
      pyrite_blog_div=opts.PYRITE_DIV_ID,
      css_dir=psettings.CSS_DIR,
      css_file=opts.CSS_FILE,
      js_dir=psettings.JS_DIR,
      pyrite_blog_js=psettings.BLOG_JS,
      pyrite_data=psettings.DATA_FILE,
      jquery=psettings.JQUERY)

