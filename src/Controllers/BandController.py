'''
Created on 14.01.2013

@author: chef
'''
import sys
from Controllers.Controller import Controller
import os.path
sys.path.append(os.path.realpath(__file__))
from Models.Tables import *
from Views import BandsView,OneBandView,BandsByLetterView

class BandController(Controller):

    View = {"get":OneBandView.OneBandView,"getAll":BandsView.BandsView,
            "getAllByLetter":BandsByLetterView.BandsByLetterView}
    
    kind = Bands
       
    @classmethod    
    def get( cls, par):  
        result = []
        query = Tracks.select().distinct().join(Bands).switch(Tracks).join(Style).where(fn.Lower(Bands.description) == par.lower())       
        result.append(cls.getResult(query,["description","style.description","length"]))
        
        divAlbs = cls.divAlbums()
        query = Albums.select().distinct().join(Bands_Album).join(Bands).where(fn.Lower(Bands.description) == par.lower(),Albums.description << divAlbs[0] )
        result.append(cls.getResult(query, ["description"])) 
        query = Albums.select().distinct().join(Bands_Album).join(Bands).where(fn.Lower(Bands.description) == par.lower(),Albums.description << divAlbs[1] ) 
        result.append(cls.getResult(query, ["description"]))
        result.append(cls.getLetters(Bands))
        return result
    
    
    
    @classmethod
    def getAll(cls, par):
        query = Bands.select()
        return cls.Result(query,["description","membersnumber"])


    @classmethod
    def getAllByLetter(cls, par):
        condition = par.lower()
        query = Bands.select().where(fn.Lower(fn.Substr(Bands.description,1,len(condition))) == condition)
        return cls.Result(query,["description","membersnumber"])
