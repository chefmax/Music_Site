'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
from os.path import dirname, realpath, sep, pardir, abspath, join
sys.path.append(abspath(join(dirname(realpath(__file__)), pardir)))
from Models import TrackModel
from Views import OneTrackView,TracksByLetterView,TracksView

class TrackController(Controller):
    View = {"get":OneTrackView.OneTrackView,"getAll":TracksView.TracksView,
            "getAllByLetter":TracksByLetterView.TracksByLetterView}
    
    Model = TrackModel.TrackModel
        