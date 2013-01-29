'''
Created on 14.01.2013

@author: chef
'''
import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))

class Controller:
    
    Controller = None
    Model = None
    View = None
    
    @classmethod
    def getController(cls):pass

    def getModel():	pass

    def getView():	pass	
    
    def get( self, req , meth, par,root_url): pass