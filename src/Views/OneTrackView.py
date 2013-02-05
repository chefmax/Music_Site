# -*- coding: utf-8 -*- 
'''
Created on 15.01.2013

@author: chef
'''
import sys 
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from Views.AbstractView import AbstractView


class OneTrackView(AbstractView):
    head = u"Песня"
    kind = "tracks"
    headers = [[u"Название песни",u"Стиль"],[u"Формат",u"Битрейт",u"Цена"],[u"Альбомы"],[u"Сборники"]]
    hrefs = [[u"download",None],[u"download",None],[u"albums"],[u"albums"]] 
    
