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


class BandsByLetterView(AbstractView):
    
    @classmethod
    def getAll(cls, tab , root_url  , stringTemplate):
        cls.Init()
        head = u"Группы на букву '%s':"  %(stringTemplate)
        chars = tab[len(tab)-1]
        result = []
        tab.pop()
        cls.addTable(result, tab[0], [u"Название группы",u"Число участников"],["bands",None])
        lettersToInsert = cls.letters.render(root_path = root_url, row = chars,kind = "bands")
        return cls.layout.render( lettersContent = lettersToInsert,
                             content = cls.tables.render(tables = result,  root_path = root_url),
                             title = head,root_path = root_url, kind = "bands" , last = cls.lastTryToFound) 
