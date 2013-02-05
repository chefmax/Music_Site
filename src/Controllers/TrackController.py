'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
from os.path import dirname, realpath, sep, pardir, abspath, join
sys.path.append(abspath(join(dirname(realpath(__file__)), pardir)))
from Models.Tables import *
from Views import OneTrackView,TracksByLetterView,TracksView

class TrackController(Controller):
    View = {"get":OneTrackView.OneTrackView,"getAll":TracksView.TracksView,
            "getAllByLetter":TracksByLetterView.TracksByLetterView}

    kind = Tracks
    
    @classmethod
    def get( cls, par):
        result = []
        query = Tracks.select(Tracks.id,Tracks.description,Tracks.style).where(fn.Lower(Tracks.description) == par.lower())
        result.append(cls.getResult(query, ["description","style.description"]))        
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
        query = Albums.select().distinct().join(Tracks_Album).join(Tracks).where(fn.Lower(Tracks.description) == par.lower(),Albums.description << divAlbs[0] )
        result.append(cls.getResult(query, ["description"])) 
        query = Albums.select().distinct().join(Tracks_Album).join(Tracks).where(fn.Lower(Tracks.description) == par.lower(),Albums.description << divAlbs[1] )
        result.append(cls.getResult(query, ["description"]))
        result.append(cls.getLetters(Tracks)) 
        return result
        
    @classmethod
    def getAll( cls, par):
        query = Tracks.select(Tracks.description,Tracks.band,Tracks.style,Tracks.length).distinct().join(Style).switch(Tracks).join(Bands)
        return cls.Result(query,["description","band.description","style.description","length"])

    @classmethod
    def getAllByLetter( cls, par):
        condition = par.lower()
        query = Tracks.select(Tracks.description,Tracks.band,Tracks.style,Tracks.length).distinct().join(Style).switch(Tracks).join(Bands).where(fn.Lower(fn.Substr(Tracks.description,1,len(condition))) == condition)
        cls.toFind = par    
        return cls.Result(query,["description","band.description","style.description","length"]) 