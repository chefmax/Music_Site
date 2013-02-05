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
    getImage = False
    lastTryToFound = ""
    layout = None
    tables = None
    letters = None
    head = ""
    kind = ""
    headers = []
    hrefs = []
    img = None
        
    @classmethod
    def addTable(cls,result,table,head,hrefs):
        parameter = []
        parameter.append(table)
        parameter.append(head)
        parameter.append(hrefs)
        result.append(parameter)
    
    @classmethod 
    def Init(cls,stringTemplate):    
        env = Environment()
        env.loader = FileSystemLoader(dirname(realpath(__file__)) + "/templates")
        cls.layout = env.get_template("layout.html")
        cls.tables = env.get_template("tables.html")
        cls.letters = env.get_template("letters.html")
        if cls.getImage == True:
                image = env.get_template("img.html")
                cls.img = image.render(path = "/band_img/" + stringTemplate)
        
    @classmethod
    def getAll(cls, tab , root_url  , stringTemplate):
        cls.Init(stringTemplate)
        chars = tab[len(tab)-1]
        result = []
        tab.pop()
        head = ""
        if stringTemplate != None:
            head = cls.head  + " '%s':" %(stringTemplate)
        for i in range(len(cls.headers)):
            cls.addTable(result, tab[i], cls.headers[i], cls.hrefs[i])
        lettersToInsert = cls.letters.render(root_path = root_url, row = chars, kind = cls.kind)
        return cls.layout.render( lettersContent = lettersToInsert ,image = cls.img,
                             content = cls.tables.render(tables = result,  root_path = root_url),
                             title = head,root_path = root_url, kind = cls.kind , last = cls.lastTryToFound) 