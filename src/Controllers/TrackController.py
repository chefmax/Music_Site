'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
from os.path import dirname, realpath, sep, pardir, abspath, join
sys.path.append(abspath(join(dirname(realpath(__file__)), pardir)))
import Models


class TrackController(Controller):
    
    @classmethod
    def getController(cls):
        if cls.Controller == None:
            cls.Controller = TrackController()
        return cls.Controller   
        
    # TODO
    # Переписать!
    def get( self, req , method, par):
        model = Models.TrackModel.TrackModel.getModel()
        try:
            getattr(model, method)()
        except Exception, e:
            return "Error! This method doesn't exist!"
            
