##############################
# Default Options for Pyrite #
##############################

#----- Basic Information -----#
BLOG_NAME = "PyriteBlog"
INPUT_LOCATION = "/Users/Kashomon/Desktop/Current Projects/pyrite/pyrite/test_files"
OUTPUT_LOCATION = "/Users/Kashomon/Desktop/Current Projects/pyrite/pyrite/test_files/pyrite_output"
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

########################
# Template Information #
########################

#----- Created files -----#
INDEX_FILE = "pyrite_index.html"
# Available templates: [basic.css, simple.css]
CSS_FILE = "ci2.css"

###################
# CSS Information #
###################

# All the Pyrite info gets stuffed into the Pyrite Div Id
BLOG_DIV_ID = "pyrite_blog"
BLOG_TITLE_CLASS = "pyrite_blog_title"

POST_CLASS = "pyrite_post" 
CONTENT_CLASS = "pyrite_content"
TITLE_CLASS = "pyrite_title"
TAGS_CLASS = "pyrite_tags"
DATE_CLASS = "pyrite_date"

ARCHIVE_BAR = "pyrite_archive"
ARCHIVE_LINK = "pyrite_archive_link"
