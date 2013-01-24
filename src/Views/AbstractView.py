# -*- coding: utf-8 -*- 
'''
Created on 15.01.2013

@author: chef
'''
import sys 
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
import re
from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2.environment import Environment

class AbstractView(object):
    
    View = None
    NumberOfLevels = 0
    LevelsUp = ""
    
    @classmethod
    def getView(cls):pass
      
        
    
    def get(self, req, parameter ,typeOfLink , header): pass
    
    def getParams(self,req):
        unparsed_parameters = "".join(req.args)
        template = re.compile("[^?&\/=]+")            
        return  template.findall(unparsed_parameters)
    
    
        
    def generateLetters(self,typeOfLink,rows):
        toBeInserted = ""    
        if typeOfLink == "albumsbyletter":
            BandsOrAlbums = "Albums"
        else:
            BandsOrAlbums = "Bands"
        for j in range(self.NumberOfLevels):
             self.LevelsUp += pardir
             self.LevelsUp += sep
        for i in rows:
            toBeInserted += "<a href = \""+ self.LevelsUp + BandsOrAlbums + "/" + str(i)[3:len(str(i))-3].replace("'", "") + "\"" + ">" +str(i)[3:len(str(i))-3].replace("'", "") + "</a>  &nbsp;"     
        return toBeInserted  
    
    
    
    
    def getHeader(self,result):
        header = result[len(result)-1]
        result.pop()
        return header

    
    def getTypeOfSample(self,req,parameter):
        if parameter == "Track_Name":
            return "tracks"
        elif parameter == "Band_Name":
            return "bands"
        else:
            return "albums"
    
    def getAll(self, req, parameter ,typeOfLink, NumberOfLevels ):
        self.NumberOfLevels = NumberOfLevels
        self.LevelsUp = ""
        env = Environment()
        env.loader = FileSystemLoader(dirname(realpath(__file__)) + "/templates")
        
        layout = env.get_template("layout")
        tables = env.get_template("tables")
        
        if (parameter != None):
            head = parameter[len(parameter)-1][0]
            parameter.pop()
        else:
            head = "Root"    
        return layout.render(content = tables.render(tables = parameter,  Levels = NumberOfLevels),title = head,Levels = NumberOfLevels ) 