# -*- coding: utf-8 -*- 
'''
Created on 15.01.2013

@author: chef
'''
import sys 
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2.environment import Environment
from Views.AbstractView import AbstractView


class AlbumView(AbstractView):
      
    @classmethod
    def getAll(cls, parameter , root_url  , stringTemplate):
        env = Environment()
        env.loader = FileSystemLoader(dirname(realpath(__file__)) + "/templates")
        layout = env.get_template("layout.html")
        tables = env.get_template("tables.html")
        letters = env.get_template("letters.html")
        head = parameter[len(parameter)-1][0]
        parameter.pop()
        chars = parameter[len(parameter)-1]
        parameter.pop()
        lettersToInsert = letters.render(root_path = root_url, row = chars)

        return layout.render( lettersContent = lettersToInsert,
                             content = tables.render(tables = parameter,  root_path = root_url),
                             title = head,root_path = root_url, kind = "albums" , last = cls.lastTryToFound ) 
