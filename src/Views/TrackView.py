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
from Views.AbstractView import AbstractView


class TrackView(AbstractView):
    
    View = None

    
    @classmethod
    def getView(cls):pass
      
        
    
    def getParams(self,req):
        unparsed_parameters = "".join(req.args)
        template = re.compile("[^?&\/=]+")            
        return  template.findall(unparsed_parameters)
      
    
    
    def getHeader(self,result):
        header = result[len(result)-1]
        result.pop()
        return header


    def getAll(self, parameter , root_url  , stringTemplate):
        env = Environment()
        env.loader = FileSystemLoader(dirname(realpath(__file__)) + "/templates")
        layout = env.get_template("layout")
        tables = env.get_template("tables")
        letters = env.get_template("letters")
        head = parameter[len(parameter)-1][0]
        parameter.pop()
        chars = parameter[len(parameter)-1]
        parameter.pop()
        lettersToInsert = letters.render(root_path = root_url, row = chars)
        return layout.render( lettersContent = lettersToInsert,
                             content = tables.render(tables = parameter,  root_path = root_url),
                             title = head,root_path = root_url, kind = "tracks" , last = self.lastTryToFound) 
