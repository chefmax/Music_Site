'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
from os.path import dirname, realpath, sep, pardir, abspath, join
sys.path.append(abspath(join(dirname(realpath(__file__)), pardir)))
import Models
from Views import TrackView

class TrackController(Controller):

    def getModel(self):
        if self.Model is None:
            self.Model = Models.TrackModel.TrackModel()
        return self.Model
    
    def getView(self):
        if self.View is None:
            self.View =  TrackView.TrackView()
        return self.View

    @classmethod
    def getController(cls):
        if cls.Controller == None:
            cls.Controller = TrackController()
        return cls.Controller   
        
    # TODO
    # rewrite
    def get( self, req , method, par,root_url):
        model = self.getModel()
        try:
            request = getattr(model, method)(req,par)  
            theView = self.getView()
            theView.lastTryToFound = model.toFind
            return theView.getAll(request , root_url,"")
        except Exception, e:
            return "Error! This method doesn't exist!"
            
