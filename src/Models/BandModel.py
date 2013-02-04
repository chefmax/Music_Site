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

class BandModel(AbstractModel):
    @classmethod
    def getLetters( cls ):
        query = Bands.select(fn.Substr(Bands.description,1,1).alias("fl")).distinct().order_by(Bands.description)
        table = []
        for iter in query:
            table.append(iter.fl.lower())
        return table
    
    @classmethod    
    def getResult(cls,condition):
        result = []
        if condition == None:
            query = Bands.select(Bands.description,Bands.membersnumber)
        else:
            query = Bands.select(Bands.id,Bands.description,Bands.membersnumber).where(fn.Lower(fn.Substr(Bands.description,1,len(condition))) == condition)
            
        table = []
        buf = []
        for iter in query:
            buf.append(iter.description)
            buf.append(iter.membersnumber)
            table.append(buf)
            buf = []
        result.append(table)  
        result.append(cls.getLetters())
        return  result
    
    
    
    @classmethod    
    def get( cls, par):   
        query = Tracks.select(Tracks.description,Tracks.length,Tracks.band,Tracks.style).distinct().join(Bands).switch(Tracks).join(Style).where(fn.Lower(Bands.description) == par.lower())
        table = []
        row = []
        for iter in query:
            row.append(iter.description)
            row.append(iter.style.description)
            row.append(iter.length)
            table.append(row)
            row = []
        result = []        
        result.append(table)
        
        divAlbs = cls.divAlbums()
        own = []
        misc = []
        query = Albums.select(Albums.description).distinct().join(Bands_Album).join(Bands).where(fn.Lower(Bands.description) == par.lower())
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
    def getAll(cls, par):
        return cls.getResult(None)

    @classmethod
    def getAllByLetter(cls, par):
        cls.toFind = par
        return cls.getResult(par.lower())
