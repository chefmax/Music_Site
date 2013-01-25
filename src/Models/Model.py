# -*- coding: utf-8 -*- 
'''
Created on 14.01.2013

@author: chef
'''
import sys
import sqlite3
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
import re
from mod_python import apache

class Model:
    
    connection = None
    
    Model = None
    
    @classmethod
    def getModel(cls):
        if cls.Model == None:
            cls.Model = Model()
        return cls.Model    
    
    def getLevel(self,req):
        unparsed_parameters = "".join(req.args)
        template = re.compile("[^?&\/=]+")            
        return  len(template.findall(unparsed_parameters))/2
    
    
    def addTitle(self,TitleContent ,result ):
        if len(result[0]) == 0:
            TitleContent = "No such"
        Title = [TitleContent]
        result.append(Title)
        return result
    
    def getConnection (self):
        #if self.connection == None:
        self.connection = sqlite3.connect(dirname(realpath(__file__)) + "/Band.db")
        return self.connection
    
    def getResult(self, request):
        buffer = request.fetchall()
        table = []
        row = []
        for i in buffer:
            for j in i:
                row.append(str(j))
            table.append(row)
            row = []
        return table    
    
    
    
    def executeLetters (self, query, header, kind , hrefs):
        result = []
        connection = self.getConnection()
        cursor = connection.cursor()
        request = cursor.execute(query)
        row = []
        for i in request:
            for j in i:
                row.append(str(j))
        result.append(row)
        result.append(header)
        result.append(hrefs) 
        result.append(kind)   
        return result
    
    
    def execute (self, query, header, kind , hrefs):
        result = []
        connection = self.getConnection()
        cursor = connection.cursor()
        request = cursor.execute(query)
        result.append(self.getResult(request))
        result.append(header)
        result.append(hrefs) 
        result.append(kind)   
        return result
    

    def get( self, req , par): pass

    def getAll(self, req , par): pass

    def getAllByLetter(self, req , par): pass


print dirname(realpath(__file__))



