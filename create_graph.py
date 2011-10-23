#!/usr/bin/python

import os 
from datetime import datetime
import string

fname = "pyrite_graph" 
file = open(fname + ".dot", "r+")
contents = file.read()
file.close()

now = datetime.now()
new_contents = string.replace(contents, "datecreated", "\"Last Generated:\\n" +
        now.isoformat() + "\"")

file = open(fname + ".dot", "w")
file.write(new_contents)
file.close()

os.system("dot -Tpdf " + fname + ".dot -o " + fname + ".pdf")
