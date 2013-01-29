'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
import Models
from Views import AlbumView

class AlbumController(Controller):

    def getModel(self):
        if self.Model is None:
            self.Model = Models.AlbumModel.AlbumModel()
        return self.Model

    def getView(self):
        if self.View is None:
            self.View = AlbumView.AlbumView()
        return self.View
    
    @classmethod
    def getController(cls):
        if cls.Controller == None:
            cls.Controller = AlbumController()
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
