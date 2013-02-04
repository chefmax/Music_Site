'''
Created on 31.01.2013

@author: chef
'''
import sys
from peewee  import *
from os.path import dirname, realpath, sep, pardir
from Tables import *
sys.path.append(dirname(realpath(__file__)))

class AbstractModel(object):
    toFind = ""
    @classmethod
    def get( cls,  par):	pass
   
    @classmethod
    def getAll( cls,  par): pass
   
    @classmethod
    def getAllByLetter( cls,  par): pass
   
    @classmethod
    def getResult(cls,title,condition): pass
   
    @classmethod
    def getLetters(cls): pass    
   
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

