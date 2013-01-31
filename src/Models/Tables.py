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
    style = ForeignKeyField(Style)
    cost = IntegerField()
    band = ForeignKeyField(Bands)       

class Track_Format(BaseModel):
    track = ForeignKeyField(Tracks)
    format = ForeignKeyField(Formats)
    bitrate = IntegerField()

class Tracks_Album(BaseModel):    
    track = ForeignKeyField(Tracks)
    album = ForeignKeyField(Albums)   
        