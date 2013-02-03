'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
from os.path import dirname, realpath, sep, pardir, abspath, join
sys.path.append(abspath(join(dirname(realpath(__file__)), pardir)))
from Models import *
from Views import TrackView

class TrackController(Controller):
        
    # TODO
    # rewrite
    @classmethod
    def get( cls,  method, par,root_url):
        try:
            request = getattr(TrackModel.TrackModel, method)(par)  
            TrackView.TrackView.lastTryToFound = TrackModel.TrackModel.toFind
            return TrackView.TrackView.getAll(request , root_url,"")
        except Exception, e:
            return "Error! This method doesn't exist!"
        