'''
Created on 14.01.2013

@author: chef
'''
import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))

class Controller:
    
    Controller = None
    
    @classmethod
    def getController(cls):pass
    
    def get( self, req , meth, par): pass