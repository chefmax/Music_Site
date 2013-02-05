# -*- coding: utf-8 -*- 
'''
Created on 15.01.2013

@author: chef
'''
import sys 
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from Views.AbstractView import AbstractView


class AlbumsView(AbstractView):
    head = u"Все альбомы:"
    kind = "albums"
    headers = [[u"Альбомы"],[u"Сборники"]]
    hrefs = [[u"albums"],[u"albums"]] 
