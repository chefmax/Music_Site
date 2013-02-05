'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
import os.path
sys.path.append(os.path.realpath(__file__))
from Models import BandModel
from Views import BandsView,OneBandView,BandsByLetterView

class BandController(Controller):

    View = {"get":OneBandView.OneBandView,"getAll":BandsView.BandsView,
            "getAllByLetter":BandsByLetterView.BandsByLetterView}
    
    Model = BandModel.BandModel