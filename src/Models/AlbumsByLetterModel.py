'''
Created on 20.01.2013

@author: chef
'''
import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from Models.Model import Model

class AlbumsByLetterModel(Model):
    
    @classmethod
    def getModel(cls):
        if cls.Model == None:
            cls.Model = AlbumsByLetterModel()
        return cls.Model
    
    
    def get( self, req , par):
        query = "SELECT distinct substr(Description,1,1) FROM Albums group by Description order by Description"
        header = [""]
        TitleContent = "Album's first letters:"
        return self.addTitle(TitleContent, self.execute(query, header))