'''
Created on 14.01.2013

@author: chef
'''
import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from Models.Model import Model

class AlbumModel(Model):
    
    
    @classmethod
    def getModel(cls):
        if cls.Model == None:
            cls.Model = AlbumModel()
        return cls.Model
    
    def get( self, req , par):
        query = """select distinct tracks.description as track, Bands.description as owner,  Style.description as style , tracks.length as length 
               from tracks, Style, Bands, Albums, tracks_album
               where tracks.Style = style.id and Bands.id = Tracks.band_id
                     and Albums.id = tracks_album.album_id and Tracks.id = tracks_album.track_id and Albums.Description like '%s'
 
            """ % (par)
        header = ["Track_Name","Owner","Style","Length"]
        TitleContent = "Album is \"%s\"" % (par)
        return self.addTitle(TitleContent, self.execute(query, header))

    def getAll( self, req , par):
        result = []
        query = """select distinct  Description from Albums,
                     (select distinct  album_id as id  , count(album_id) as count from  tracks_album
                      group by album_id ) t1
                   where t1.id = Albums.id and t1.count = 1   
         """
        header = ["Album_Name"]
        
        result.extend(self.execute(query, header))
        
        query = """select distinct  Description from Albums,
                     (select distinct  album_id as id  , count(album_id) as count from  tracks_album
                      group by album_id ) t1
                   where t1.id = Albums.id and t1.count > 1   
         """
        header = ["Miscellanys"]
        
        result.extend(self.execute(query, header))
        
        TitleContent = "All albums:"       
        return self.addTitle(TitleContent, result)

    def getAllByLetter( self, req , par):
        query = "select distinct  Description from Albums where description like '%s'" % (par+'%')
        header = ["Album_Name"]
        TitleContent = "All albums by \"%s\":" % (par) 
        return self.addTitle(TitleContent, self.execute(query, header))