'''
Created on 31.01.2013

@author: chef
'''
import sys
from peewee  import *
from os.path import dirname, realpath, sep, pardir
from Tables import *
sys.path.append(dirname(realpath(__file__)))
import re

class AbstractModel(object):
    toFind = ""
    def get( self, req , par):	pass

    def getAll( self, req , par): pass

    def getAllByLetter( self, req , par): pass

    def getResult(self,title,condition): pass

    def getLetters(self): pass    

    def addTitle(self,TitleContent ,result ):
        if len(result[0]) == 0:
            TitleContent = "No such"
        Title = [TitleContent]
        result.append(Title)
        return result
    
    
    def addTable (self, table,header, kind , hrefs):
        result = []
        result.append(table)
        result.append(header)
        result.append(hrefs) 
        result.append(kind)   
        return result    

    def divAlbums(self,cond):
        if cond == None:
            query = Tracks_Album.select(Tracks_Album.album,Tracks_Album.track,Tracks).distinct().join(Tracks).join(Bands).switch(Tracks_Album).join(Albums)
        else:
            query = Tracks_Album.select(Tracks_Album.album,Tracks_Album.track,Tracks).distinct().join(Tracks).join(Bands).switch(Tracks_Album).join(Albums).where(Tracks_Album.album << cond)
        albums = []
        misc  = []
        own = []
        for i in query:
           try:
               ind = albums.index(str(i.album.description))
               albums[ind] = "#" + str(i.album.description)
           except Exception,e:
               try:
                   ind = albums.index("#" + str(i.album.description))
               except Exception:
                   albums.append(str(i.album.description))
        for albs in albums:
            if albs[0] == "#":
                misc.append([albs[1:]])
            else:
                own.append([albs])
        albums = []
        albums.append(own)
        albums.append(misc)
        return albums 
              