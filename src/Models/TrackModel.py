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
    
    def get( self, req , par):
        result = []
        
        query = """select distinct tracks.description, style.description from tracks,style
                   where tracks.style = style.id and tracks.description like '%s'
                 """ % (par)
        header = ["Track_name","Style"]
        result.extend(self.execute(query, header))
        
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
        header = ["Format","Bitrate","Cost"]
        
        result.extend(self.execute(query, header))
        query = """ select distinct  albums.description from albums,tracks, tracks_album,
                        (select distinct  album_id as id  , count(bands.id) as count from  tracks_album,bands,tracks
                         where tracks_album.track_id = tracks.id and tracks.band_id = bands.id  
                         group by tracks_album.album_id ) t1
                    where tracks.description like '%s' and tracks_album.track_id = tracks.id 
                    and tracks_album.album_id = albums.id  and t1.count > 1 and t1.id = albums.id 
                """ % (par)
        header = ["Miscellanys"]
        result.extend(self.execute(query, header))
        query = """ select distinct  albums.description from albums,tracks, tracks_album,
                        (select distinct  album_id as id  , count(bands.id) as count from  tracks_album,bands,tracks
                         where tracks_album.track_id = tracks.id and tracks.band_id = bands.id  
                         group by tracks_album.album_id  ) t1
                    where tracks.description like '%s' and tracks_album.track_id = tracks.id 
                    and tracks_album.album_id = albums.id  and t1.count = 1 and t1.id = albums.id 
                """ % (par)
        header = ["Band's Albums"]
        result.extend(self.execute(query, header))
        TitleContent = "Track is \"%s\"" % (par)      
        return self.addTitle(TitleContent, result)

    def getAll( self, req , par):
        query ="""select distinct  Tracks.Description as Name, Style.Description as Style, Tracks.length as Length 
                  from Tracks, Bands, Style
                  where Tracks.band_id = Bands.id and Style.id = Tracks.style"""
        header = ["Track_Name","Style","Length"]
        TitleContent = "All tracks:"
        return self.addTitle(TitleContent, self.execute(query, header))

    def getAllByLetter( self, req , par):
        query ="""select distinct  Tracks.Description as Name, Style.Description as Style, Tracks.length as Length 
                  from Tracks, Bands, Style
                  where Tracks.band_id = Bands.id and Style.id = Tracks.style and Tracks.description like '%s'
               """ % (par+'%')
        header = ["Track_Name","Style","Length"]
        TitleContent = "All tracks by \"%s\":" % (par) 
        return self.addTitle(TitleContent, self.execute(query, header))   