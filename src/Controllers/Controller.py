'''
Created on 14.01.2013

@author: chef
'''
import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from Models.Tables import *
from Views import AbstractView
class Controller:
    
    View = {"get":AbstractView.AbstractView,"getAll":AbstractView.AbstractView,"getAllByLetter":AbstractView.AbstractView}  
    toFind = ""
    kind = ""
    @classmethod
    def getRequest( cls,  method, par, root_url):
        try:
            request = getattr(cls, method)(par)  
            cls.View[method].lastTryToFound = cls.toFind
            return cls.View[method].getAll(request , root_url,par)
        except Exception, e:
            print e
    
    
    
    @classmethod  
    def getLetters( cls , From ):
        query = From.select(fn.Substr(From.description,1,1).alias("fl")).distinct().order_by(From.description)
        table = []
        for iter in query:
            table.append(iter.fl.lower())
        return table
    
    @classmethod
    def divAlbums(cls):
        query = Bands_Album.select(Bands_Album.band,Bands_Album.album).distinct()
        albums = []
        misc  = []
        own = []
        for iter in query:
            if iter.album.description in own:
                own.remove(iter.album.description)
                if iter.album.description not in misc:
                    misc.append(iter.album.description)
            elif iter.album.description not in misc:
                own.append(iter.album.description)
                
        albums.append(own)
        albums.append(misc)
        return albums 
    
    @classmethod
    def Result(cls,query,attributes):
        result = []
        result.append(cls.getResult(query,attributes))
        result.append(cls.getLetters(cls.kind))
        return result
    
    @classmethod
    def atr(cls,object,name):
        pos = name.find(".")
        if pos == -1:
            return getattr(object, name)
        else:
            return getattr(getattr(object, name[0:pos]),name[pos+1:])
    
    @classmethod
    def getResult(cls,query,attributes):
        table = []
        buf = []
        for iter in query:
            for at in attributes:
                buf.append(cls.atr(iter, at))
            table.append(buf)
            buf = []
        return table    

    
    
    