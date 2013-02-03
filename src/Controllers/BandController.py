'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
import os.path
sys.path.append(os.path.realpath(__file__))
from Models import *
from Views import BandView

class BandController(Controller):
    
    @classmethod
    def get( cls,  method, par, root_url):
      #  try:
        request = getattr(BandModel.BandModel, method)(par)  
        BandView.BandView.lastTryToFound = BandModel.BandModel.toFind
        return BandView.BandView.getAll(request , root_url,par)
       # except Exception, e:
        #    return "Error! This method '%s' doesn't exist!" %(method)