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

class TrackModel(AbstractModel):
    
    @classmethod  
    def getLetters( cls ):
        query = Tracks.select(fn.Substr(Tracks.description,1,1).alias("fl")).distinct().order_by(Tracks.description)
        table = []
        for iter in query:
            table.append(iter.fl.lower())
        return table
    
    @classmethod
    def getResult(cls,condition):
        result = []
        if condition == None:
            query = Tracks.select(Tracks.description,Tracks.band,Tracks.style,Tracks.length).distinct().join(Style).switch(Tracks).join(Bands)
        else:
            query = Tracks.select(Tracks.description,Tracks.band,Tracks.style,Tracks.length).distinct().join(Style).switch(Tracks).join(Bands).where(fn.Lower(fn.Substr(Tracks.description,1,len(condition))) == condition)
            
        table = []
        buf = []
        for iter in query:
            buf.append(iter.description)
            buf.append(iter.band.description)
            buf.append(iter.style.description)
            buf.append(iter.length)
            table.append(buf)
            buf = []
        result.append(table)
        result.append(cls.getLetters())
        return result

    @classmethod
    def get( cls, par):
        result = []
        query = Tracks.select(Tracks.id,Tracks.description,Tracks.style)
        table = []
        row = []
        for iter in query:
            if (str(iter.description).lower() == par.lower()):
                row.append(iter.description)
                row.append(iter.style.description)
        table.append(row)
        result.append(table)
        
        table = []
        rows = []
        
        query = Track_Format.select(Track_Format.format,Track_Format.track,Track_Format.bitrate).distinct().join(Formats).switch(Track_Format).join(Tracks).where(fn.Lower(Tracks.description) == par.lower())
        for iter in query:
            rows.append(iter.format.description)
            rows.append(iter.bitrate)
            if iter.bitrate > 128:
                rows.append(iter.track.cost * 2)
            else:    
                rows.append(iter.track.cost)
            table.append(rows)
            rows = []    
                    
        result.append(table)
        
        divAlbs = cls.divAlbums()
        own = []
        misc = []
        query = Albums.select(Albums.description).distinct().join(Tracks_Album).join(Tracks).where(fn.Lower(Tracks.description) == par.lower())
        for iter in query:
            if iter.description in divAlbs[0]:
                own.append([iter.description])
            else:
                misc.append([iter.description])
        result.append(own)
        result.append(misc)
        result.append(cls.getLetters()) 
        return result
        
    @classmethod
    def getAll( cls, par):
        return cls.getResult(None)

    @classmethod
    def getAllByLetter( cls, par):
        cls.toFind = par    
        return cls.getResult( par.lower()) 