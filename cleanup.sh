#!/bin/bash
# clean up some biles

find . -name '*.pyc' -print | xargs rm 
find . -name '*~' -print | xargs rm 

rm -rf 'Pyrite.egg-info'
rm -rf 'dist'
rm -rf 'build' 
