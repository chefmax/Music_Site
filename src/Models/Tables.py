'''
Created on 30.01.2013

@author: chef
'''
import datetime
from peewee import *
from os.path import dirname, realpath, sep, pardir , isdir
from os import listdir
import sqlite3


class BaseModel(Model):
    """A base model that will use our Sqlite database"""
    sqlite_db = SqliteDatabase(dirname(realpath(__file__))+'/db/Band.db',check_same_thread=False)
    class Meta:
        database = SqliteDatabase(dirname(realpath(__file__))+'/db/Band.db',check_same_thread=False)


class StrField(Field):
    db_field = 'text'
    def python_value(self,v):
        return str(v)
    
    def lower(self):
        return self.python_value(self).lower() 

class Albums(BaseModel):
    description = TextField()

class BlobField(Field):
    db_field = 'blob'
    
    def db_value(self, v):
        return sqlite3.Binary(v)

class Bands(BaseModel):
    description = TextField()
    membersnumber = IntegerField()
    img = BlobField()  



class Formats(BaseModel):
    description = TextField()
    
class Style(BaseModel):
    description = TextField()

class Tracks(BaseModel):
    description = TextField()
    length = TextField()
    style = ForeignKeyField(Style,related_name='style')
    cost = IntegerField()
    band = ForeignKeyField(Bands,related_name='owner')       

class Track_Format(BaseModel):
    track = ForeignKeyField(Tracks, related_name='tracks')
    format = ForeignKeyField(Formats, related_name='format')
    bitrate = IntegerField()

class Tracks_Album(BaseModel):    
    track = ForeignKeyField(Tracks, related_name='tracks')
    album = ForeignKeyField(Albums, related_name='albums')   

class Bands_Album(BaseModel):    
    band = ForeignKeyField(Bands, related_name='bands')
    album = ForeignKeyField(Albums, related_name='albums')   
        
        