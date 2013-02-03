'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from Models import *

class CssJsController(Controller):

    @classmethod
    def get( cls, method, par,root_url):
        return getattr(CssJsModel.CssJsModel, "get")(par)



