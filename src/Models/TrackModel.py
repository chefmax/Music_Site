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

class TrackModel(AbstractModel):
  
    def getLetters( self ):
        query = Tracks.select(Tracks.description)
        table = []
        for iter in query:
            table.append(str(iter.description)[0].lower())
        table = list(set(table))
        table.sort()
        header = [""]
        kind = [u"tracks"]
        hrefs = [0]
        return self.addTable(table, header, kind, hrefs)
    
    def getResult(self,title,condition):
        result = []
        hrefs = [0,0,-4,-4]
        kind = [u"tracks",u"bands",None,None]
        header = [u"Название песни",u"Автор",u"Стиль",u"Длина"]
        if condition == None:
            query = Tracks.select(Tracks.description,Tracks.band,Tracks.style,Tracks.length).distinct().join(Style).switch(Tracks).join(Bands)
        else:
            query = Tracks.select(Tracks.description,Tracks.band,Tracks.style,Tracks.length).distinct().join(Style).switch(Tracks).join(Bands).where(Tracks.id << condition)
            
        table = []
        buf = []
        for iter in query:
            buf.append(iter.description)
            buf.append(iter.band.description)
            buf.append(iter.style.description)
            buf.append(iter.length)
            table.append(buf)
            buf = []
        TitleContent = title
        result.append(self.addTable(table, header, kind, hrefs))  
        result.append(self.getLetters())
        return self.addTitle(TitleContent, result)

    
    def get( self, req , par):
        result = []
        hrefs = [0,-4]
        kind = [u"download",None]
        header = [u"Название песни",u"Стиль"]
        query = Tracks.select(Tracks.id,Tracks.description,Tracks.style)
        table = []
        cond = []
        row = []
        for iter in query:
            if (str(iter.description).lower() == par.lower()):
                row.append(iter.description)
                row.append(iter.style.description)
                cond.append(iter.id)
        table.append(row)
        result.append(self.addTable(table, header, kind, hrefs))
        
        table = []
        rows = []
        hrefs = [0,-4,-4]
        header = [u"Формат",u"Битрейт",u"Цена"]
        kind = [u"download",None,None]
        
        query = Track_Format.select(Track_Format.format,Track_Format.track,Track_Format.bitrate).distinct().join(Formats).switch(Track_Format).join(Tracks).where(Track_Format.track << cond)
        for iter in query:
            rows.append(iter.format.description)
            rows.append(iter.bitrate)
            if iter.bitrate > 128:
                rows.append(iter.track.cost * 2)
            else:    
                rows.append(iter.track.cost)
            table.append(rows)
            rows = []    
                    
        result.append(self.addTable(table, header, kind, hrefs))
        
        cond = []
        condquery = Tracks.select(Tracks.id,Tracks.description)
        for it in condquery:
            if str(it.description).lower() == par.lower():
                cond.append(Tracks.id)
        divAlbs = self.divAlbums(cond)
        
        hrefs = [0]

        kind = [u"albums"]
        header = [u"Альбомы"]
        result.append(self.addTable(divAlbs[0], header, kind, hrefs))
        header = [u"Сборники"]
        result.append(self.addTable(divAlbs[1], header, kind, hrefs)) 
        result.append(self.getLetters())
        TitleContent = u"Песня \"%s\":" % (par) 
        return self.addTitle(TitleContent, result) 
        
    def getAll( self, req , par):
        return self.getResult(u"Все песни:",None)

    def getAllByLetter( self, req , par):
        self.toFind = par
        condquery = Tracks.select(Tracks)
        cond = []
        for iter in condquery:
            if str(iter.description).lower().find(par.lower()) == 0:
                cond.append(iter.id)
        title = u"Все песни на букву \"%s\":" % (str(par))        
        return self.getResult(title , cond) 