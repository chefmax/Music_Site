# -*- coding: utf-8 -*- 
'''
Created on 14.01.2013

@author: chef
'''
import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from Models.Model import Model
import sqlite3

class BandImgModel(Model):
    
    @classmethod
    def getModel(cls):
        if cls.Model == None:
            cls.Model = BandImgModel()
        return cls.Model
    
    def get( self, req , par):
        query = "SELECT distinct img FROM Bands where description like '%s'" %(par)
        cursor = self.getConnection().cursor()       
        return cursor.execute(query).fetchone()[0]
