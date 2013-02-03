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
        header = [""]
        kind = [u"bands"]
        hrefs = [0]
        return cls.addTable(table, header, kind, hrefs)
    
    @classmethod    
    def getResult(cls,title,condition):
        result = ["0"]
        hrefs = [0,-4]
        kind = ["bands",None]
        header = [u"Название группы",u"Число участников"]
        TitleContent = u"Группы:"
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
        TitleContent = title
        result.append(cls.addTable(table, header, kind, hrefs))  
        result.append(cls.getLetters())
        return cls.addTitle(TitleContent, result)
    
    
    
    @classmethod    
    def get( cls, par):
        result = ["1"]
        hrefs = [0,-4,-4] 
        kind = [u"tracks",None,None]
        header = [u"Название песни",u"Стиль",u"Длина"]
        
        query = Tracks.select(Tracks.description,Tracks.length,Tracks.band,Tracks.style).distinct().join(Bands).switch(Tracks).join(Style).where(fn.Lower(Bands.description) == par.lower())
        table = []
        row = []
        for iter in query:
            row.append(iter.description)
            row.append(iter.style.description)
            row.append(iter.length)
            table.append(row)
            row = []
                
        result.append(cls.addTable(table, header, kind, hrefs))
        
        divAlbs = cls.divAlbums()
        own = []
        misc = []
        query = Albums.select(Albums.description).distinct().join(Bands_Album).join(Bands).where(fn.Lower(Bands.description) == par.lower())
        for iter in query:
            if iter.description in divAlbs[0]:
                own.append([iter.description])
            else:
                misc.append([iter.description])
        hrefs = [0]
        kind = [u"albums"]
        header = [u"Альбомы"]
        result.append(cls.addTable(own, header, kind, hrefs))
        header = [u"Сборники"]
        result.append(cls.addTable(misc, header, kind, hrefs)) 
        result.append(cls.getLetters())
        TitleContent = u"Группа \"%s\":" % (par) 
        return cls.addTitle(TitleContent, result) 
    @classmethod
    def getAll(cls, par):
        return cls.getResult(u"Группы:",None)

    @classmethod
    def getAllByLetter(cls, par):
        cls.toFind = par
        condquery = Bands.select(Bands.description,Bands.id)
        cond = []
        for iter in condquery:
            if str(iter.description).lower().find(str(par).lower()) == 0:
                cond.append(iter.id)
        TitleContent = u"Группы на букву \"%s\":" % (par)
        return cls.getResult(TitleContent,par.lower())
