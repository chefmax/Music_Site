'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from Models import *
from Views import AlbumView

class AlbumController(Controller):
    
    @classmethod
    def get( cls,  method, par,root_url):
        try:
            request = getattr(AlbumModel.AlbumModel, method)(par)
            AlbumView.AlbumView.lastTryToFound = AlbumModel.AlbumModel.toFind
            return AlbumView.AlbumView.getAll(request , root_url, "")
        except Exception, e:
            return "Error! This method doesn't exist!"
