#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

import default_options 
import file_util
import os
import sys

def init_or_read_opts(input_dir, output_dir, clean_init):
    if not indir_is_initd(input_dir):
        init_indir(input_dir)
        print "Finished initializing Pyrite. Have fun Pyriting!" 
        sys.exit(0) 

    if clean_init:
        init_indir(input_dir)

    print "Checking for output directory initialization"

    sys.exit(0)
    # init_outdir_if_needed(output_dir)


def indir_is_initd(input_dir):
    file_set = frozenset(os.listdir(input_dir))
    if "pyrite_options.py" not in file_set:
        return False 
    else: 
        return True
     

def init_indir(input_dir):
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
    
    print '' 
    print 'What will be the URL of your website? ' 
    website_url = raw_input('[default=www.pyrite-blog.com]: ')
    if website_url == '': website_url = 'www.pyrite-blog.com'
    options = options.replace('my_website_url', website_url)
    print '------------------'
    print 'Writing your options to pyrite_options.py'
    print '------------------'
    

    file_util.write_file(
        os.path.join(input_dir, "pyrite_options.py"), options)



def read_options():
    to_read = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "templates",
        "default_options.py")
    return file_util.read_file(to_read)


def init_outdir_if_needed(out_dir):
    pass


def make_in_dirs(in_dir): 
    pass

def make_out_dirs(out_dir):
    file_util.makedirs_quiet(os.path.join(input_dir, "pyrite_css"))
    file_util.makedirs_quiet(os.path.join(input_dir, "pyrite_js"))
