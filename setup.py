# Copyright (c) 2011 by Joshua Hoak
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

from setuptools import setup, find_packages
from pyrite import __version__
import os
    
setup(name='Pyrite',
    version=__version__,
    description='A static blog creator.',
    author='Josh Hoak',
    author_email='jrhoak@gmail.com',
    url='https://github.com/Kashomon/pyrite',
    license='MIT',
    install_requires=['argparse', 'mako'],
    packages=["pyrite"],
    package_data={"pyrite" : [
      os.path.join("resources","*.html"),
      os.path.join("resources","js","*.js"),
      os.path.join("resources","css","*.css"),
      os.path.join("resources","html","*.css"),
      os.path.join("resources","media","*")]},
    entry_points="""
    [console_scripts]
    pyrite = pyrite.main:main 
    """
    )   

