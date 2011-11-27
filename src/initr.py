#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import file_util
import os
import sys
import imp

OPTIONS_NAME = "pyrite_options.py"
CSS_DIR = "pyrite_css" 
JS_DIR = "pyrite_js" 
MEDIA_DIR = "pyrite_media"
DIRS = [CSS_DIR, JS_DIR, MEDIA_DIR]

TEMP_DIR = "templates"

DEFAULT_OPTS = "default_options.py"

BLOG_JS_TEMP = "pyrite_blog_template.js"
INDEX_TEMP = "index_template.html"
CSS_TEMP = "basic.css"
CSS_OUT = "pyrite.css"
JQUERY = "jquery-1.7.1.min.js"

DATA_FILE = "pyrite_data.js"
BLOG_JS = "pyrite_blog.js"

#For Reference: From the Options file:
#INDEX_FILE = "index.html"
#CSS_FILE = "pyrite.css"

def init_or_read_opts(input_dir, output_dir, clean_init):
    if not indir_is_initd(input_dir) and not clean_init:
        init_indir(input_dir)
        print "Finished initializing Pyrite. Have fun Pyriting!" 

    if clean_init:
        clean_dirs(input_dir, output_dir) 
        init_indir(input_dir)

    options = read_and_import_options(input_dir)

    init_outdir_if_needed(output_dir, options)

    return options


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
    options = read_default_options()
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

def read_default_options():
    to_read = os.path.join(
        file_util.get_module_dir(),
        TEMP_DIR,
        DEFAULT_OPTS)
    return file_util.read_file(to_read)

def read_and_import_options(input_dir):
    options_mod = None
    opts_file = os.path.join(input_dir, OPTIONS_NAME)
    print "Importing the options file"
    try: 
        options_mod = imp.load_source("options", opts_file)
    except ImportError:
        print "Couldn't import the options file: %s" % opts_file
        sys.exit(2)
    except IOError:
        print "Couldn't find the specified options file: %s" % opts_file
    return options_mod

def init_outdir_if_needed(out_dir, opts):
    print '------------------'
    print "Checking for output directory initialization"
    print '------------------'
    ensure_base_dir_exists(out_dir)
    make_out_dirs(out_dir)
    
    mod_dir = file_util.get_module_dir()    

    # TODO: Clean this up!
    blog_js_path = os.path.join(out_dir, JS_DIR, BLOG_JS)
    if not os.path.isfile(blog_js_path):
        blog_js = file_util.read_file(
            os.path.join(mod_dir, TEMP_DIR, JS_DIR, BLOG_JS_TEMP))
        file_util.write_file(blog_js_path, blog_js)

    index_path = os.path.join(out_dir, opts.INDEX_FILE) 
    if not os.path.isfile(index_path):
        index = file_util.read_file(
            os.path.join(mod_dir, TEMP_DIR, INDEX_TEMP))
        file_util.write_file(index_path, index)

    css_path = os.path.join(out_dir, CSS_DIR, opts.CSS_FILE)
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
    file_util.remove_file(os.path.join(input_dir, OPTIONS_NAME))
    file_util.remove_file(os.path.join(output_dir, "pyrite_index.html"))
    for d in DIRS: 
        dir_path = os.path.join(output_dir, d)
        file_util.remove_all_files(dir_path)
        file_util.remove_dir(dir_path)
