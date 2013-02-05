# -*- coding: utf-8 -*- 
'''
Created on 15.01.2013

@author: chef
'''
import sys 
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from Views.AbstractView import AbstractView


class OneBandView(AbstractView):
    head = u"Группа "
    kind = "bands"
    headers = [[u"Название песни",u"Стиль",u"Длина"],[u"Альбомы"],[u"Сборники"]]
    hrefs = [[u"tracks",None,None],[u"albums"],[u"albums"]] 
    getImage = True
