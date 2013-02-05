'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
from os.path import dirname, realpath, sep, pardir, abspath, join
sys.path.append(abspath(join(dirname(realpath(__file__)), pardir)))
from Models.Tables import *
from Views import OneAlbumView,AlbumsByLetterView,AlbumsView

class AlbumController(Controller):
    View = {"get":OneAlbumView.OneAlbumView,"getAll":AlbumsView.AlbumsView,
            "getAllByLetter":AlbumsByLetterView.AlbumsByLetterView}
    
    kind = Albums
    
    @classmethod    
    def getAlbums(cls, condition):
        result = []
        div = cls.divAlbums()
        albums = []
        misc = []
        if condition == None:
            for album in div[0]:
                albums.append([album]) 
            for album in div[1]:
                misc.append([album])
        else:
            for album in div[0]:
                if album.lower().find(condition) == 0:
                    albums.append([album]) 
            for album in div[1]:
                if album.lower().find(condition) == 0:
                    misc.append([album]) 
                       
        result.append(albums)  
        result.append(misc)    
        result.append(cls.getLetters(Albums))    
        return result
    
    @classmethod    
    def get( cls, par):
        result = []     
        query = Tracks.select().distinct().join(Tracks_Album).join(Albums).switch(Tracks).join(Bands).switch(Tracks).join(Style).where(fn.Lower(Albums.description) == par.lower())
        result.append(cls.getResult(query, ["description","band.description","style.description","length"])) 
        result.append(cls.getLetters(Albums))
        return result
    
    @classmethod
    def getAll( cls, par):
        return cls.getAlbums(None)
    
    @classmethod
    def getAllByLetter( cls, par):
        cls.toFind = par
        return cls.getAlbums( par.lower())  
    
        