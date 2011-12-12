#!/usr/bin/python
# Copyright (c) 2011 Joshua Hoak
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import sys
from mako.template import Template

from . import file_util
from . import psettings

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
      pyrite_blog_id=opts.BLOG_DIV_ID,
      css_dir=psettings.CSS_DIR,
      css_file=opts.CSS_FILE,
      js_dir=psettings.JS_DIR,
      pyrite_blog_js=psettings.BLOG_JS,
      pyrite_data=psettings.DATA_FILE,
      jquery=psettings.JQUERY)

def css_render(template, opts):
  return template.render(
      pyrite_blog_id=opts.BLOG_DIV_ID,
      post_class=opts.POST_CLASS,
      content_class=opts.CONTENT_CLASS,
      title_class=opts.TITLE_CLASS,
      tags_class=opts.TAGS_CLASS,
      date_class=opts.DATE_CLASS,
      blog_title_class=opts.BLOG_TITLE_CLASS,
      archive_bar=opts.ARCHIVE_BAR,
      archive_link=opts.ARCHIVE_LINK)

def render_blog(template, title, opts):
  return template.render(
      blog_title_class=opts.BLOG_TITLE_CLASS,
      rendered_blog_title=title,
      pyrite_blog_id=opts.BLOG_DIV_ID,
      archive_bar=opts.ARCHIVE_BAR)


