'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
import os.path
sys.path.append(os.path.realpath(__file__))
import Models
from Views import BandView

class BandController(Controller):
    def getModel(self):
        if self.Model == None:
            self.Model = Models.BandModel.BandModel()
        return self.Model

    def getView(self):
        if self.View == None:
            self.View = BandView.BandView()
        return self.View   
    
    @classmethod
    def getController(cls):
        if cls.Controller == None:
            cls.Controller = BandController()
        return cls.Controller 

    def get( self, req , method, par, root_url):
        model = self.getModel()
        try:
            request = getattr(model, method)(req,par)  
            theView = self.getView()
            theView.lastTryToFound = model.toFind
            return theView.getAll(request , root_url,par)
        except Exception, e:
            return "Error! This method '%s' doesn't exist!" %(method)