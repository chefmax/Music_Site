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


class AlbumsByLetterView(AbstractView):
    
    @classmethod
    def getAll(cls, tab , root_url  , stringTemplate):
        cls.Init()
        head = u"Альбомы на букву '%s':" % (stringTemplate)
        result = []
        chars = tab[len(tab)-1]
        tab.pop()
        cls.addTable(result, tab[0], [u"Альбомы"], [u"albums"])
        cls.addTable(result, tab[1], [u"Сборники"], [u"albums"])
        lettersToInsert = cls.letters.render(root_path = root_url, row = chars, kind = "albums")
        return  cls.layout.render(lettersContent = lettersToInsert,
                             content = cls.tables.render(tables = result,  root_path = root_url),
                             title = head,root_path = root_url, kind = "albums" , last = cls.lastTryToFound) 
