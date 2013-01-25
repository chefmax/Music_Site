# -*- coding: utf-8 -*- 
'''
Created on 14.01.2013

@author: chef
'''
import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from Models.Model import Model

class BandModel(Model):
    
    @classmethod
    def getModel(cls):
        if cls.Model == None:
            cls.Model = BandModel()
        return cls.Model
    
    
    def getLetters( self, req ):
        query = "SELECT distinct substr(Description,1,1) FROM Bands group by Description order by Description"
        header = [""]
        kind = ["bands"]
        hrefs = [0]
        return (self.executeLetters(query, header,kind,hrefs))
    
    
    def get( self, req , par):
        result = []
        hrefs = [0,-4,-4] 
        kind = ["tracks",None,None]
        query = """select distinct tracks.description as track, Style.description as style , tracks.length as length 
                   from tracks, Style, Bands
                   where tracks.Style = style.id and Bands.id = Tracks.band_id and bands.description like '%s'
                """ % (par)
        header = [u"Название песни",u"Стиль",u"Длина"]
        
        result.append(self.execute(query, header,kind,hrefs))
        
        hrefs = [0]
        kind = ["albums"]
        query = """select distinct Albums.description  
                   from tracks, Albums, Bands, tracks_album 
                   where Bands.id = Tracks.band_id and bands.description like '%s' 
                         and tracks.id = tracks_album.track_id and tracks_album.album_id = albums.id
                """ % (par)
        header = [u"Название альбома"]
        result.append(self.execute(query, header,kind,hrefs))
        
        TitleContent = u"Группа \"%s\"" % (par)
        result.append(self.getLetters(req))
        return self.addTitle(TitleContent, result)

    def getAll(self, req , par):
        result = []
        hrefs = [0,-4]
        kind = ["bands",None]
        query = "select distinct  Description, MembersNumber from Bands"
        header = [u"Название группы",u"Число участников"]
        TitleContent = u"Группы:"        
        result.append(self.execute(query, header,kind,hrefs))
        result.append(self.getLetters(req))
        return self.addTitle(TitleContent, result)

    def getAllByLetter(self, req , par):
        result = []
        hrefs = [0,-4]
        kind = ["bands",None]
        query = "select distinct Description, MembersNumber from Bands where description like '%s'" % (par+'%')
        header = [u"Название группы",u"Число участников"]
        TitleContent = u"Группы на букву \"%s\":" % (par)
        result.append(self.execute(query, header,kind,hrefs))
        result.append(self.getLetters(req))
        return self.addTitle(TitleContent, result)