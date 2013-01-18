'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
import Models

class AlbumController(Controller):
    
    @classmethod
    def getController(cls):
        if cls.Controller == None:
            cls.Controller = AlbumController()
        return cls.Controller 
    
    def get( self, req , method, par):
        model = Models.AlbumModel.AlbumModel.getModel()
        if method == "get":
            return model.get(req,par)
        elif method == "getAll":
            return model.getAll(req,par)
        elif method == "getAllByLetter":
            return model.getAllByLetter(req,par)
        else:
            return "Error! This method doesn't exist!"

