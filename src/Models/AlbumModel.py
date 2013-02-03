# -*- coding: utf-8 -*- 
'''
Created on 14.01.2013

@author: chef
'''
import sys
from peewee  import *
from os.path import dirname, realpath, sep, pardir
from Tables import *
sys.path.append(dirname(realpath(__file__)))
from AbstractModel import AbstractModel

class AlbumModel(AbstractModel):        

    @classmethod    
    def getLetters( cls ):
        query = Albums.select(fn.Substr(Albums.description,1,1).alias("fl")).distinct().order_by(Albums.description)
        table = []
        for iter in query:
            table.append(iter.fl.lower())
        return table
   
    @classmethod    
    def getResult(cls, condition):
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
        result.append(cls.getLetters())    
        return result
    
    @classmethod    
    def get( cls, par):
        result = []     
        table = []
        buf = []
        query = Tracks_Album.select(Tracks_Album.album,Tracks_Album.track,Tracks).distinct().join(Tracks).join(Bands).switch(Tracks_Album).join(Albums).where(fn.Lower(Albums.description) == par.lower())
        for iter in query:
            buf.append(iter.track.description)
            buf.append(iter.track.band.description)
            buf.append(iter.track.style.description)
            buf.append(iter.track.length)
            table.append(buf)
            buf = []
       
        result.append(table)  
        result.append(cls.getLetters())
        return result
    
    @classmethod
    def getAll( cls, par):
        return cls.getResult(None)
    
    @classmethod
    def getAllByLetter( cls, par):
        cls.toFind = par
        return cls.getResult( par.lower())  