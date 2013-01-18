'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
sys.path.append("/home/chef/workspace/Music_Site/src")
import Models

class BandController(Controller):
    
    @classmethod
    def getController(cls):
        if cls.Controller == None:
            cls.Controller = BandController()
        return cls.Controller 
    
    def get(self, req , meth, par):
        model = Models.BandModel.BandModel.getModel()
        if meth == "get":
            return model.get(req, par)
        elif meth == "getAll":
            return model.getAll(req, par)
        elif meth == "getAllByLetter":
            return model.getAllByLetter(req,par)
        else:
            return "Error! This method doesn't exist!"