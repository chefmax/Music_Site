# -*- coding: utf-8 -*- 
'''
Created on 14.01.2013

@author: chef
'''
import sys
from peewee  import *
from os.path import dirname, realpath, sep, pardir
from Tables import *
sys.path.append(dirname(realpath(__file__)))
import re
from AbstractModel import AbstractModel


class BandImgModel(AbstractModel):
    
    @classmethod
    def getModel(cls):
        if cls.Model == None:
            cls.Model = BandImgModel()
        return cls.Model
    
    def get( self, req , par):
        res =  Bands.select(Bands.img,Bands.description)
        for iter in res:
            if str(iter.description).lower() == par.lower():
                return iter.img
