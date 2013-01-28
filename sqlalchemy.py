import datetime
from peewee import *
from os.path import dirname, realpath, sep, pardir , isdir
from os import listdir


sqlite_db = SqliteDatabase(dirname(realpath(__file__))+'/src/Models/Band.db')

class BaseModel(Model):
    """A base model that will use our Sqlite database"""
    class Meta:
        database = sqlite_db


class Band(BaseModel):
    description = TextField()
    membersnumber = IntegerField()


sqlite_db.connect()