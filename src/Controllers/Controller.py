'''
Created on 14.01.2013

@author: chef
'''
import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
from Models import AbstractModel
from Views import AbstractView
class Controller:
    
    View = {"get":AbstractView.AbstractView,"getAll":AbstractView.AbstractView,"getAllByLetter":AbstractView.AbstractView}  
    Model = AbstractModel.AbstractModel
    @classmethod
    def getView(cls,method):
        return cls.View[method]
    
    @classmethod
    def get( cls,  method, par, root_url):
        try:
            request = getattr(cls.Model, method)(par)  
            cls.getView(method).lastTryToFound = cls.Model.toFind
            return cls.getView(method).getAll(request , root_url,par)
        except Exception, e:
            print e.value