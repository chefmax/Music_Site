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
        query ="select distinct  Description from Albums"
        header = ["Album_Name"]
        TitleContent = "All albums:"       
        return self.addTitle(TitleContent, self.execute(query, header))

    def getAllByLetter( self, req , par):
        query = "select distinct  Description from Albums where description like '%s'" % (par+'%')
        header = ["Album_Name"]
        TitleContent = "All albums by \"%s\":" % (par) 
        return self.addTitle(TitleContent, self.execute(query, header))