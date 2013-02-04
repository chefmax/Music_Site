'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
from os.path import dirname, realpath, sep, pardir, abspath, join
sys.path.append(abspath(join(dirname(realpath(__file__)), pardir)))
from Models import *
from Views import OneTrackView,TracksByLetterView,TracksView

class TrackController(Controller):
    @classmethod
    def getView(cls,method):
        if method == "get":
            return OneTrackView.OneTrackView
        elif method == "getAll":
            return TracksView.TracksView
        else:
            return TracksByLetterView.TracksByLetterView        
    
    
    @classmethod
    def get( cls,  method, par,root_url):
        try:
            request = getattr(TrackModel.TrackModel, method)(par)  
            cls.getView(method).lastTryToFound = TrackModel.TrackModel.toFind
            return cls.getView(method).getAll(request , root_url,par)
        except Exception, e:
            return "Error! This method doesn't exist!"
        