# -*- coding: utf-8 -*- 
'''
Created on 15.01.2013

@author: chef
'''
import sys 
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
import re
from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2.environment import Environment

class CssJsView(object):
    
    View = None
    NumberOfLevels = 0
    LevelsUp = ""
    
    @classmethod
    def getView(cls):pass
      
        
    
    def get(self, req, parameter ,typeOfLink , header): pass

    def getAll(self, req, parameter ,method, root_url , kindOf , stringTemplate):
        return parameter
