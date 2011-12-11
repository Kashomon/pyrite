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
    psettings.BLOG_JS : css_render,
    psettings.INDEX_TEMP : index_render,
    "css" : css_render,
  }

  file = "css" if file.endswith(".css") else file
  if file in render_methods:
    template = Template(filename=in_path)
    return render_methods.get(file)(template, opts)
  else:
    return file_util.read_file(in_path)

def index_render(template, opts):
  return template.render(
      pyrite_blog_id=opts.PYRITE_BLOG_ID,
      css_dir=psettings.CSS_DIR,
      css_file=opts.CSS_FILE,
      js_dir=psettings.JS_DIR,
      pyrite_blog_js=psettings.BLOG_JS,
      pyrite_data=psettings.DATA_FILE,
      jquery=psettings.JQUERY)

def css_render(template, opts):
  return template.render(
      pyrite_blog_id=opts.PYRITE_BLOG_ID,
      post_class=opts.POST_CLASS,
      content_class=opts.CONTENT_CLASS,
      title_class=opts.TITLE_CLASS,
      tags_class=opts.TAGS_CLASS,
      date_class=opts.DATE_CLASS)


