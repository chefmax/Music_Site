'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
import Models

class CssJsController(Controller):
    
    @classmethod
    def getController(cls):
        if cls.Controller == None:
            cls.Controller = CssJsController()
        return cls.Controller 
    
    def get( self, req , method, par):
        model = Models.CssJsModel.CssJsModel.getModel()
        return model.get(req,par)



