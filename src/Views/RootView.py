# -*- coding: utf-8 -*- 
'''
Created on 15.01.2013

@author: chef
'''
import sys 
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from Views.AbstractView import AbstractView


class RootView(AbstractView):
    @classmethod  
    def getAll(cls, parameter , root_url  , stringTemplate):
        cls.Init(stringTemplate)
        head = u"Добрый день!"     
        return cls.layout.render( title = head ) 
