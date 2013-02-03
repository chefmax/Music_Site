'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
import os.path
sys.path.append(os.path.realpath(__file__))
from Models import *
from Views import BandsView,OneBandView,BandsByLetterView

class BandController(Controller):
    
    @classmethod
    def getView(cls,method):
        if method == "get":
            return OneBandView.OneBandView
        elif method == "getAll":
            return BandsView.BandsView
        else:
            return BandsByLetterView.BandsByLetterView
    
    @classmethod
    def get( cls,  method, par, root_url):
      #  try:
        request = getattr(BandModel.BandModel, method)(par)  
        cls.getView(method).lastTryToFound = BandModel.BandModel.toFind
        return cls.getView(method).getAll(request , root_url,par)
       # except Exception, e:
        #    return "Error! This method '%s' doesn't exist!" %(method)