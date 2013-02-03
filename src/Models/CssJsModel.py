# -*- coding: utf-8 -*- 
'''
Created on 14.01.2013

@author: chef
'''
import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from AbstractModel import AbstractModel

class CssJsModel(AbstractModel):

    @classmethod    
    def get( cls, par):
        source = open(par,"r")
        result = source.readlines()   
        source.close()
        return result
