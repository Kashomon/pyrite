# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Authors: Josh Hoak (jrhoak@gmail.com)

from setuptools import setup, find_packages
import src
    
setup(name='Pyrite',
      version=src.__version__,
      description='A static blog creator.',
      author='Josh Hoak',
      author_email='jrhoak@gmail.com',
      url='https://github.com/Kashomon/pyrite',
      license='MIT',
      packages=["src", "src/parsing", "src/data_structures", 
      "src/templates"],
      install_requires =['argparse'],
      entry_points="""
      [console_scripts]
      pyrite = src.main:main 
      """
     )   

