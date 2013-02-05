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
        divAlbs = cls.divAlbums()
        if condition == None:
            query = Albums.select().distinct().where(Albums.description << divAlbs[0])
            result.append(cls.getResult(query, ["description"]))
            query = Albums.select().distinct().where(Albums.description << divAlbs[1])
            result.append(cls.getResult(query, ["description"]))
        else:
            query = Albums.select().distinct().where(Albums.description << divAlbs[0],fn.Substr(fn.Lower(Albums.description),1,1) == condition)
            result.append(cls.getResult(query, ["description"]))
            query = Albums.select().distinct().where(Albums.description << divAlbs[1],fn.Substr(fn.Lower(Albums.description),1,1) == condition)
            result.append(cls.getResult(query, ["description"]))
                
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
    
        