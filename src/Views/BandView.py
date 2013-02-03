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


class BandView(AbstractView):
    
    
    @classmethod  
    def getAll(cls, parameter , root_url  , stringTemplate):
        env = Environment()
        env.loader = FileSystemLoader(dirname(realpath(__file__)) + "/templates")
        layout = env.get_template("layout")
        tables = env.get_template("tables")
        letters = env.get_template("letters")
        if parameter[0] == '1':
            image = env.get_template("img")
            img = image.render(path = root_url + "band_img/" + stringTemplate)
        else:
            img = ""    
        parameter.pop(0)
        head = parameter[len(parameter)-1][0]
        parameter.pop()
        chars = parameter[len(parameter)-1]
        parameter.pop()
        lettersToInsert = letters.render(root_path = root_url, row = chars)

        return layout.render(image = img, lettersContent = lettersToInsert,
                             content = tables.render(tables = parameter,  root_path = root_url),
                             title = head,root_path = root_url, kind = "bands" , last = cls.lastTryToFound) 
