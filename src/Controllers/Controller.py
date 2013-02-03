'''
Created on 14.01.2013

@author: chef
'''
import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))

class Controller:
    
    @classmethod
    def get( cls, meth, par,root_url): pass