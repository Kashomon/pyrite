#!/usr/bin/python
##############################
# Default Options for Pyrite #
##############################


#####################
# Basic Information #
#####################
BLOG_NAME = "MyBlogName"
INPUT_LOCATION = "my_in_location"
OUTPUT_LOCATION = "my_out_location"

# For more about python date formats, see
# http://docs.python.org/library/datetime.html#strftime-and-strptime-behavior
IN_DATE_FORMAT = "%d %B %Y"     # i.e., strptime
OUT_DATE_FORMAT = "%d %B %Y"    # i.e., strftime

#######################
# Website Information #
#######################
# Example: PYRITE_WEBSITE_LOCATION = 'www.myblog.com'
PYRITE_WEBSITE_LOCATION = "my_website_url"

# Pyrite assumes by default that your blog is located at
# PYRITE_WEBSITE_LOCATION.
PYRITE_PATH = "" 

# Leave the field below blank if you're hosting website entirely in one place.
# If your static content is hosted in another place, this is useful for
# having Javascript request dynamic content.
XMLHTTP_REQUEST_LOCATION = ""  
