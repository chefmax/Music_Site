'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
import Models

class BandImgController(Controller):
    
    @classmethod
    def getController(cls):
        if cls.Controller == None:
            cls.Controller = BandImgController()
        return cls.Controller 

    def getModel(self):
        if self.Model is None:
            self.Model = Models.BandImgModel.BandImgModel()
        return self.Model    
    
    # TODO
    # rewrite!
    def get( self, req , method, par,root_url):
        model = self.getModel()
        result = getattr(model, 'get')(req,par)
        return result    
