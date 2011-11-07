#!/bin/bash
# clean up some biles

find . -name '*.pyc' -print | xargs rm 
find . -name '*~' -print | xargs rm 
