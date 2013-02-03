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


class OneTrackView(AbstractView):
    
    @classmethod
    def getAll(cls, tab , root_url  , stringTemplate):
        cls.Init()
        head = u"Песня %s:" %(stringTemplate)
        chars = tab[len(tab)-1]
        result = []
        tab.pop()
        cls.addTable(result, tab[0], [u"Название песни",u"Стиль"], [u"download",None])
        cls.addTable(result, tab[1], [u"Формат",u"Битрейт",u"Цена"], [u"download",None,None])
        cls.addTable(result, tab[2], [u"Альбомы"], [u"albums"])
        cls.addTable(result, tab[3], [u"Сборники"], [u"albums"])
        lettersToInsert = cls.letters.render(root_path = root_url, row = chars, kind = "tracks")
        return cls.layout.render( lettersContent = lettersToInsert ,
                             content = cls.tables.render(tables = result,  root_path = root_url),
                             title = head,root_path = root_url, kind = "tracks" , last = cls.lastTryToFound) 
