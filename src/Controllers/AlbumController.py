'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
from os.path import dirname, realpath, sep, pardir, abspath, join
sys.path.append(abspath(join(dirname(realpath(__file__)), pardir)))
from Models import AlbumModel
from Views import OneAlbumView,AlbumsByLetterView,AlbumsView

class AlbumController(Controller):
    View = {"get":OneAlbumView.OneAlbumView,"getAll":AlbumsView.AlbumsView,
            "getAllByLetter":AlbumsByLetterView.AlbumsByLetterView}
    
    Model = AlbumModel.AlbumModel
        