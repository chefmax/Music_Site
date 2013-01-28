# -*- coding: utf-8 -*- 
'''
Created on 14.01.2013

@author: chef
'''
import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from Models.Model import Model

class CssJsModel(Model):
    
    @classmethod
    def getModel(cls):
        if cls.Model == None:
            cls.Model = CssJsModel()
        return cls.Model
    
    def get( self, req , par):
        source = open(par,"r+")
        result = source.readlines()   
        source.close()
        return result
