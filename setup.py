# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

from setuptools import setup, find_packages
import src
import os
    
setup(name='Pyrite',
    version=src.__version__,
    description='A static blog creator.',
    author='Josh Hoak',
    author_email='jrhoak@gmail.com',
    url='https://github.com/Kashomon/pyrite',
    license='MIT',
    install_requires=['argparse', 'mako'],
    packages=["pyrite", "pyrite/data_structures", "pyrite/resources"],
    package_data={"pyrite" : ["resources/*.html", "resources/js/*.js",
    "resources/css/*.css"]},
    entry_points="""
    [console_scripts]
    pyrite = src.main:main 
    """
    )   

