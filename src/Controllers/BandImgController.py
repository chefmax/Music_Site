'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from Models.Tables import *

class BandImgController(Controller):
    
    @classmethod
    def getRequest( cls,  method, par,root_url):
        return  cls.get(par)  

    @classmethod    
    def get( cls, par):
        res =  Bands.select(Bands.img,Bands.description)
        for iter in res:
            if str(iter.description).lower() == par.lower():
                return iter.img