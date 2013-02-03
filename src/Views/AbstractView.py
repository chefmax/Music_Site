# -*- coding: utf-8 -*- 
'''
Created on 15.01.2013

@author: chef
'''
import sys 
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from jinja2 import FileSystemLoader
from jinja2.environment import Environment

class AbstractView(object):
    
    lastTryToFound = ""
    layout = None
    tables = None
    letters = None
        
    @classmethod
    def addTable(cls,result,table,head,hrefs):
        parameter = []
        parameter.append(table)
        parameter.append(head)
        parameter.append(hrefs)
        result.append(parameter)
    
    @classmethod 
    def Init(cls):    
        env = Environment()
        env.loader = FileSystemLoader(dirname(realpath(__file__)) + "/templates")
        cls.layout = env.get_template("layout.html")
        cls.tables = env.get_template("tables.html")
        cls.letters = env.get_template("letters.html")
        
    @classmethod
    def getAll(cls, parameter , root_url , stringTemplate): pass