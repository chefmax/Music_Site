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
import re
from AbstractModel import AbstractModel

class AlbumModel(AbstractModel):        
    def getLetters( self ):
        query = Albums.select(Albums.description)
        table = []
        for iter in query:
            table.append(str(iter.description)[0].lower())
        table = list(set(table))
        table.sort()
        header = [""]
        kind = [u"albums"]
        hrefs = [0]
        return self.addTable(table, header, kind, hrefs)
   
    
    def getResult(self, title, condition):
        result = []
        hrefs = [0]
        kind = [u"albums"]
        header = [u"Альбомы"]      
        result.append(self.addTable(self.divAlbums(condition)[0], header, kind, hrefs))
        header = [u"Сборники"]    
        result.append(self.addTable(self.divAlbums(condition)[1], header, kind, hrefs))    
        result.append(self.getLetters())    
        return self.addTitle(title, result)
    
    
    def get( self, req , par):
        header = [u"Название песни",u"Автор",u"Стиль",u"Длина"]
        TitleContent = u"Альбом \"%s\"." %(par)
        kind = ["tracks","bands",None,None]
        result = []
        query = ""
        hrefs = [0,0,-4,-4] 
        condquery = Albums.select(Albums)
        cond = []
        for iter in condquery:
            if str(iter.description).lower() == par.lower():
                cond.append(iter.id)        
        table = []
        buf = []
        query = Tracks_Album.select(Tracks_Album.album,Tracks_Album.track,Tracks).distinct().join(Tracks).join(Bands).switch(Tracks_Album).join(Albums).where(Tracks_Album.album << cond)
        for iter in query:
            buf.append(iter.track.description)
            buf.append(iter.track.band.description)
            buf.append(iter.track.style.description)
            buf.append(iter.track.length)
            table.append(buf)
            buf = []
       
        result.append(self.addTable(table, header, kind, hrefs))  
        result.append(self.getLetters())
        return self.addTitle(TitleContent, result)

    def getAll( self, req , par):
        return self.getResult(u"Все альбомы:", None)

    def getAllByLetter( self, req , par):
        self.toFind = par
        TitleContent = u"Альбомы на букву \"%s\":" % (par) 
        condquery = Albums.select(Albums.description,Albums.id)
        cond = []
        for iter in condquery:
            if str(iter.description).lower().find(par.lower()) == 0:
                cond.append(iter.id)
        return self.getResult(TitleContent, cond)    