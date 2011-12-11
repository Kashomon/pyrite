#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

def safe_get(di, item, elseitem):
  if item in di:
    return di[item]
  else:
    di[item] = elseitem
    return elseitem

def get_or_else(di, item, elseitem):
  if item in di:
    return di[item]
  else:
    return elseitem
