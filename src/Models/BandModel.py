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
    
    def get( self, req , par):
        result = []
        query = """select distinct tracks.description as track, Style.description as style , tracks.length as length 
                   from tracks, Style, Bands
                   where tracks.Style = style.id and Bands.id = Tracks.band_id and bands.description like '%s'
                """ % (par)
        header = ["Track_Name","Style","Length"]
        
        result.extend(self.execute(query, header))
        
        query = """select distinct Albums.description  
                   from tracks, Albums, Bands, tracks_album 
                   where Bands.id = Tracks.band_id and bands.description like '%s' 
                         and tracks.id = tracks_album.track_id and tracks_album.album_id = albums.id
                """ % (par)
        header = ["Album_Name"]
        result.extend(self.execute(query, header))
        
        return result

    def getAll(self, req , par):
        query = "select distinct  Description, MembersNumber from Bands"
        header = ["Band_Name","Number of Members"]
        return self.execute(query, header)

    def getAllByLetter(self, req , par):
        query = "select distinct Description, MembersNumber from Bands where description like '%s'" % (par+'%')
        header = ["Band_Name","Number of Members"]
        return self.execute(query, header)
