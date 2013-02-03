# -*- coding: utf-8 -*- 
'''
Created on 15.01.2013

@author: chef
'''
import sys 
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from Views.AbstractView import AbstractView
class CssJsView(AbstractView):
    
    @classmethod
    def getAll(cls, parameter , root_url  , stringTemplate):
        return parameter
