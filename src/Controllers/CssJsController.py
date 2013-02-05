'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))

class CssJsController(Controller):

    @classmethod
    def getRequest( cls, method, par,root_url):
        return cls.get(par)
    
    @classmethod    
    def get( cls, par):
        source = open(par,"r")
        result = source.readlines()   
        source.close()
        return result




