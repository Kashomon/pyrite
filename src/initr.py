#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import file_util
import os
import sys

OPTIONS_NAME = "pyrite_options.py"
CSS_DIR = "pyrite_css" 
JS_DIR = "pyrite_js" 
MEDIA_DIR = "pyrite_media"
DIRS = [CSS_DIR, JS_DIR, MEDIA_DIR]

TEMP_DIR = "templates"

DEFAULT_OPTS = "default_options.py"

DATA_FILE = "pyrite_data.js"
BLOG_JS_OUT = "pyrite_blog.js"
BLOG_JS_TEMP = "pyrite_blog_template.js"
INDEX_TEMP = "index_template.html"
INDEX_OUT = "index.html"
CSS_TEMP = "basic.css"
CSS_OUT = "pyrite.css"
JQUERY = "jquery-1.7.1.min.js"

def init_or_read_opts(input_dir, output_dir, clean_init):
    if not indir_is_initd(input_dir) and not clean_init:
        init_indir(input_dir)
        print "Finished initializing Pyrite. Have fun Pyriting!" 
        sys.exit(0) 

    if clean_init:
        clean_dirs(input_dir, output_dir) 
        init_indir(input_dir)

    init_outdir_if_needed(output_dir)


def indir_is_initd(input_dir):
    file_set = frozenset(os.listdir(input_dir))
    if OPTIONS_NAME not in file_set:
        return False 
    else: 
        return True
     

def init_indir(input_dir):
    ensure_base_dir_exists(input_dir)
    print '------------------'
    print 'Pyrite Initializer'
    print '------------------'
    options = read_options()
    print 'Let\'s initialize your blog with some initial settigns'
    print 'You can change them later in the generated pyrite_options.py'
    print ''
    print 'What do you want your blog to be called?'
    blog_name = raw_input('[default=PyriteBlog]: ')
    if blog_name == '': blog_name = 'PyriteBlog'
    print ''
    print 'Your blog will be called: %s' % blog_name
    print '------------------'
    blog_name
    options = options.replace('MyBlogName', blog_name)

    print 'Where do you want your blog-files to be read from?'
    input_location = raw_input('[default=%s]: ' % (input_dir))
    if input_location == '': input_location = input_dir
    options = options.replace('my_in_location', input_location)

    print '' 
    print 'Where do you want your generated blog-files to be put?'
    output_location = raw_input('[default=%s]: ' % (
        os.path.join(input_dir, 'pyrite_output')))
    if output_location == '': output_location = (
        os.path.join(input_dir, 'pyrite_output'))
    options = options.replace('my_out_location', output_location)
    print '------------------'
    print 'Writing your options to %s' % OPTIONS_NAME
    print '------------------'

    file_util.write_file(
        os.path.join(input_dir, OPTIONS_NAME), options)

def read_options():
    to_read = os.path.join(
        file_util.get_module_dir(),
        TEMP_DIR,
        DEFAULT_OPTS)
    return file_util.read_file(to_read)


def init_outdir_if_needed(out_dir):
    print '------------------'
    print "Checking for output directory initialization"
    print '------------------'
    ensure_base_dir_exists(out_dir)
    make_out_dirs(out_dir)
    
    mod_dir = file_util.get_module_dir()    

    # TODO: Clean this up!
    blog_js_path = os.path.join(out_dir, JS_DIR, BLOG_JS_OUT)
    if not os.path.isfile(blog_js_path):
        blog_js = file_util.read_file(
            os.path.join(mod_dir, TEMP_DIR, JS_DIR, BLOG_JS_TEMP))
        file_util.write_file(blog_js_path, blog_js)

    index_path = os.path.join(out_dir, INDEX_OUT) 
    if not os.path.isfile(index_path):
        index = file_util.read_file(
            os.path.join(mod_dir, TEMP_DIR, INDEX_TEMP))
        file_util.write_file(index_path, index)

    css_path = os.path.join(out_dir, CSS_DIR, CSS_OUT)
    if not os.path.isfile(css_path):
        css = file_util.read_file( 
            os.path.join(mod_dir, TEMP_DIR, CSS_DIR, CSS_TEMP))
        file_util.write_file(css_path, css) 

    jquery_path = os.path.join(out_dir, JS_DIR, JQUERY)
    if not os.path.isfile(jquery_path):
        jquery = file_util.read_file( 
            os.path.join(mod_dir, TEMP_DIR, JS_DIR, JQUERY))
        file_util.write_file(jquery_path, jquery) 

def ensure_base_dir_exists(path): 
   if os.path.isdir(path):
        return
   else:
        print "The directory: %s doesn't exist." % path
        make_base_dirs(path)

def make_base_dirs(path): 
   file_util.makedirs_quiet(path) 

def make_out_dirs(out_dir):
    for direct in DIRS:
        file_util.makedirs_quiet(os.path.join(out_dir, direct))

def clean_dirs(input_dir, output_dir): 
    print 'Cleaning the pyrite-produced files'

    opts = os.path.join(input_dir, OPTIONS_NAME) 
    file_util.remove_file(opts)
    index = os.path.join(output_dir, INDEX_OUT)
    file_util.remove_file(index)
    for d in DIRS: 
        dir_path = os.path.join(output_dir, d)
        file_util.remove_all_files(dir_path)
        file_util.remove_dir(dir_path)
