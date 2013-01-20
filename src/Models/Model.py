'''
Created on 14.01.2013

@author: chef
'''
import sys
import sqlite3
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))

class Model:
    
    connection = None
    
    Model = None
    
    @classmethod
    def getModel(cls):
        if cls.Model == None:
            cls.Model = Model()
        return cls.Model    
    
    def addTitle(self,TitleContent ,result ):
        if len(result[0]) == 0:
            TitleContent = "No such"
        Title = [TitleContent]
        result.extend(Title)
        return result
    
    def getConnection (self):
        #if self.connection == None:
        self.connection = sqlite3.connect('/home/chef/workspace/www/Band.db')
        return self.connection
    
    def execute (self, query, header):
        result = []
        connection = self.getConnection()
        cursor = connection.cursor()
        request = cursor.execute(query)
        result.append(request.fetchall())
        result.append(header)
        return result
    

    def get( self, req , par): pass

    def getAll(self, req , par): pass

    def getAllByLetter(self, req , par): pass






