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
        query = """ select distinct   tracks.description as track,Formats.description as format, bitrate as bitrate,Style.description as style,tracks.cost  
                from tracks,Track_Format,Formats,Style
                where tracks.id = Track_Format.track_id and Track_Format.bitrate<128 
                      and Track_Format.format_id = Formats.id and tracks.Style = style.id and tracks.description like '%s'
                union
                select distinct   tracks.description as track,Formats.description as format, bitrate as bitrate,Style.description as style,2*tracks.cost   
                from tracks,Track_Format,Formats,Style
                where tracks.id = Track_Format.track_id and Track_Format.bitrate>=128 
                      and Track_Format.format_id = Formats.id and tracks.Style = style.id and tracks.description like '%s'
 
            """ % (par,par)
        header = ["Track_Name","Format","Bitrate","Style","Cost"]
        result = []
        result.extend(self.execute(query, header))
        query = """ select distinct  albums.description from albums,tracks, tracks_album
                    where tracks.description like '%s' and tracks_album.track_id = tracks.id 
                    and tracks_album.album_id = albums.id
                """ % (par)
        header = ["Album_Name"]
        result.extend(self.execute(query, header))
        return result

    def getAll( self, req , par):
        query ="""select distinct  Tracks.Description as Name, Style.Description as Style, Tracks.length as Length 
                  from Tracks, Bands, Style
                  where Tracks.band_id = Bands.id and Style.id = Tracks.style"""
        header = ["Track_Name","Style","Length"]
        return self.execute(query, header)

    def getAllByLetter( self, req , par):
        query ="""select distinct  Tracks.Description as Name, Style.Description as Style, Tracks.length as Length 
                  from Tracks, Bands, Style
                  where Tracks.band_id = Bands.id and Style.id = Tracks.style and Tracks.description like '%s'
               """ % (par+'%')
        header = ["Track_Name","Style","Length"]
        return self.execute(query, header)   