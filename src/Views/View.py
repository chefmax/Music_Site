# -*- coding: utf-8 -*- 
'''
Created on 17.01.2013

@author: chef
'''
import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
import re
from Views.AbstractView import AbstractView
import sqlite3
from jinja2 import Template

class View(AbstractView):
    
    def writeLetters (self, connection, cursor, typeOfLink, LevelsUp):
        if typeOfLink == "albumsbyletter":
            BandsOrAlbums = "Albums"
        else:
            BandsOrAlbums = "Bands"  
        cursor.execute("SELECT distinct substr(Description,1,1) FROM %s group by Description order by Description" % (BandsOrAlbums) )
        FirstLetters = []
        result = ""
        for i in cursor:
            resultToString = str(i)
            FirstLetters.append(resultToString[3:len(resultToString)-3])
        for i in FirstLetters :
            result += "<a href=\"" + LevelsUp + BandsOrAlbums + "> " + i +" </a> &nbsp;"
        return result    
    
    
    
    @classmethod  
    def getView(cls):
        if cls.View == None:
            cls.View = View()
        return cls.View  

            
        
 