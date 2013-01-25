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
      
    
    
    def getHeader(self,result):
        header = result[len(result)-1]
        result.pop()
        return header


    def getAll(self, req, parameter ,typeOfLink, NumberOfLevels ):
        self.NumberOfLevels = NumberOfLevels
        self.LevelsUp = ""
        env = Environment()
        env.loader = FileSystemLoader(dirname(realpath(__file__)) + "/templates")
        
        layout = env.get_template("layout")
        tables = env.get_template("tables")
        letters = env.get_template("letters")
        if (parameter != None):
            head = parameter[len(parameter)-1][0]
            parameter.pop()
            chars = parameter[len(parameter)-1]
            parameter.pop()
            lettersToInsert = letters.render(Levels = NumberOfLevels, row = chars)
        else:
            head = "Root" 
            lettersToInsert = ""
         
        return layout.render(lettersContent = lettersToInsert,
                             content = tables.render(tables = parameter,  Levels = NumberOfLevels),
                             title = head,Levels = NumberOfLevels ) 
