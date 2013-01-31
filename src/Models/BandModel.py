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

class BandModel(AbstractModel):
    
    def getLetters( self ):
        query = Bands.select(Bands.description).order_by(Bands.description)
        table = []
        for iter in query:
            table.append(str(iter.description)[0].lower())
        table = list(set(table))
        table.sort()
        header = [""]
        kind = [u"bands"]
        hrefs = [0]
        return self.addTable(table, header, kind, hrefs)
    
    
    def getResult(self,title,condition):
        result = ["0"]
        hrefs = [0,-4]
        kind = ["bands",None]
        header = [u"Название группы",u"Число участников"]
        TitleContent = u"Группы:"
        if condition == None:
            query = Bands.select(Bands.description,Bands.membersnumber)
        else:
            query = Bands.select(Bands.id,Bands.description,Bands.membersnumber).where(Bands.id << condition)
            
        table = []
        buf = []
        for iter in query:
            buf.append(iter.description)
            buf.append(iter.membersnumber)
            table.append(buf)
            buf = []
        #print table
        TitleContent = title
        result.append(self.addTable(table, header, kind, hrefs))  
        result.append(self.getLetters())
        return self.addTitle(TitleContent, result)
    
    
    
    
    def get( self, req , par):
        result = ["1"]
        hrefs = [0,-4,-4] 
        kind = [u"tracks",None,None]
        header = [u"Название песни",u"Стиль",u"Длина"]
        
        query = Tracks.select(Tracks.description,Tracks.length,Tracks.band,Tracks.style).join(Bands).switch(Tracks).join(Style)
        table = []
        cond = []
        row = []
        for iter in query:
            if (str(iter.band.description).lower() == par.lower()):
                row.append(iter.description)
                row.append(iter.style.description)
                row.append(iter.length)
                cond.append(iter.id)
            table.append(row)
            row = []
                
        result.append(self.addTable(table, header, kind, hrefs))
        
        condquery = Bands.select(Bands.id,Bands.description)
        for it in condquery:
            if str(it.description).lower() == par.lower():
                cond.append(Bands.id)
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

    def getAll(self, req , par):
        return self.getResult(u"Группы:",None)


    def getAllByLetter(self, req , par):
        self.toFind = par
        condquery = Bands.select(Bands.description,Bands.id)
        cond = []
        for iter in condquery:
            if str(iter.description).lower().find(str(par).lower()) == 0:
                cond.append(iter.id)
        TitleContent = u"Группы на букву \"%s\":" % (par)
        return self.getResult(TitleContent,cond)