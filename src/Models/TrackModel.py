# -*- coding: utf-8 -*- 
'''
Created on 14.01.2013

@author: chef

'''
import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from Models.Model import Model

class TrackModel(Model):
    
    @classmethod
    def getModel(cls):
        if cls.Model == None:
            cls.Model = TrackModel()
        return cls.Model
    
    
    def getLetters( self, req ):
        query = "SELECT distinct substr(Description,1,1) FROM Tracks group by Description order by Description"
        header = [""]
        kind = [u"tracks"]
        hrefs = [0]
        return (self.executeLetters(query, header,kind,hrefs))
    
    
    def get( self, req , par):
        result = []
        hrefs = [0,-4,-4]
        kind = [u"download",None]
        query = """select distinct tracks.description, style.description from tracks,style
                   where tracks.style = style.id and tracks.description like '%s'
                 """ % (par)
        header = [u"Название песни",u"Стиль"]
        result.append(self.execute(query, header,kind,hrefs))
        
        query = """ select distinct Formats.description as format, bitrate as bitrate,tracks.cost  
                from tracks,Track_Format,Formats,Style
                where tracks.id = Track_Format.track_id and Track_Format.bitrate<128 
                      and Track_Format.format_id = Formats.id and tracks.Style = style.id and tracks.description like '%s'
                union
                select distinct Formats.description as format, bitrate as bitrate,2*tracks.cost   
                from tracks,Track_Format,Formats,Style
                where tracks.id = Track_Format.track_id and Track_Format.bitrate>=128 
                      and Track_Format.format_id = Formats.id and tracks.Style = style.id and tracks.description like '%s'
 
            """ % (par,par)
        header = [u"Формат",u"Битрейт",u"Цена"]
        kind = [u"download",None,None]
        result.append(self.execute(query, header,kind,hrefs))
        hrefs = [0]
        query = """ select distinct  albums.description from albums,tracks, tracks_album,
                        (select distinct  album_id as id  , count(bands.id) as count from  tracks_album,bands,tracks
                         where tracks_album.track_id = tracks.id and tracks.band_id = bands.id  
                         group by tracks_album.album_id ) t1
                    where tracks.description like '%s' and tracks_album.track_id = tracks.id 
                    and tracks_album.album_id = albums.id  and t1.count > 1 and t1.id = albums.id 
                """ % (par)
        header = [u"Сборники"]
        kind = [u"albums"]
        result.append(self.execute(query, header,kind,hrefs))
        query = """ select distinct  albums.description from albums,tracks, tracks_album,
                        (select distinct  album_id as id  , count(bands.id) as count from  tracks_album,bands,tracks
                         where tracks_album.track_id = tracks.id and tracks.band_id = bands.id  
                         group by tracks_album.album_id  ) t1
                    where tracks.description like '%s' and tracks_album.track_id = tracks.id 
                    and tracks_album.album_id = albums.id  and t1.count = 1 and t1.id = albums.id 
                """ % (par)
        header = [u"Альбомы"]
        result.append(self.execute(query, header,kind,hrefs))
        TitleContent = u"Песня \"%s\"" % (par)    
        result.append(self.getLetters(req))  
        return self.addTitle(TitleContent, result)

    def getAll( self, req , par):
        result = []
        hrefs = [0,0,-4,-4]
        kind = [u"tracks",u"bands",None,None]
        query ="""select distinct  Tracks.Description as Name,Bands.description as Owner, Style.Description as Style, Tracks.length as Length 
                  from Tracks, Bands, Style
                  where Tracks.band_id = Bands.id and Style.id = Tracks.style"""
        header = [u"Название песни",u"Автор",u"Стиль",u"Длина"]
        TitleContent = u"Все песни:"
        result.append(self.execute(query, header,kind,hrefs))
        result.append(self.getLetters(req))
        return self.addTitle(TitleContent, result)

    def getAllByLetter( self, req , par):
        result = []
        kind = [u"tracks",u"bands",None,None]
        hrefs = [0,0,-4,-4]
        query ="""select distinct  Tracks.Description as Name,Bands.description as Owner, Style.Description as Style, Tracks.length as Length 
                  from Tracks, Bands, Style
                  where Tracks.band_id = Bands.id and Style.id = Tracks.style and Tracks.description like '%s'
               """ % (par+'%')
        header = [u"Название песни",u"Автор",u"Стиль",u"Длина"]
        TitleContent = u"Все песни на букву \"%s\":" % (par) 
        result.append(self.execute(query, header,kind,hrefs))
        result.append(self.getLetters(req))        
        return self.addTitle(TitleContent, result)