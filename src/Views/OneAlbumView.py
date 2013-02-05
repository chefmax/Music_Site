# -*- coding: utf-8 -*- 
'''
Created on 15.01.2013

@author: chef
'''
import sys 
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from Views.AbstractView import AbstractView


class OneAlbumView(AbstractView):
    
    head = u"Альбом:"
    kind = "albums"
    headers = [[u"Название песни",u"Автор",u"Стиль",u"Длина"]]
    hrefs = [["tracks","bands",None,None]] 