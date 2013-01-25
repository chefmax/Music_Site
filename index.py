# -*- coding: utf-8 -*- 
from mod_python import apache
import sqlite3
import time
import re
import sys
from os.path import dirname, realpath, sep, pardir , isdir
from os import listdir 
for name in listdir(dirname(realpath(__file__))):
    if isdir(name):
        sys.path.append(realpath(__file__) + sep + str(name))
sys.path.append(dirname(realpath(__file__)) + sep + "src")
from Controllers import *
from Models import *
from Views import *

def getController(kind_of_controller):
    if kind_of_controller.lower() == "albums":
        return AlbumController.AlbumController.getController()
    elif kind_of_controller.lower() == "bands":
        return BandController.BandController.getController()
    elif kind_of_controller.lower() == "tracks":
        return TrackController.TrackController.getController()
    elif kind_of_controller.lower() == "albumsbyletter":
        return AlbumsByLetterController.AlbumsByLetterController.getController()
    elif kind_of_controller.lower() == "bandsbyletter":
        return BandsByLetterController.BandsByLetterController.getController()


def getParams(req):
        unparsed_parameters = "".join(req.args)
        template = re.compile("[^?&\/=]+")            
        return  template.findall(unparsed_parameters)
    


def getMethod(numberOfParameters,parameters):
    if numberOfParameters == 2:
        return "getAll"
    elif numberOfParameters == 4 or (numberOfParameters == 6 and parameters[4] == "num" ):
        return "getAllByLetter"
    else:
        return "get"

def getTemplate(parameters):
    method = getMethod(len(parameters),parameters)
    if method == "get":
        return parameters[5]
    elif method == "getAllByLetter":
        return parameters[3]
    else:
        return None


def getLevel(params):
    if params[len(params)-2] == "num":
        return int(params[len(params)-1])
    else:
        return len(params)/2

def getresult(req, params,root_url):  
    if params == None:
        TheView = View.View()
        return TheView.getAll(req,None,None,root_url,None)
    else:
        TheController = getController(params[1])
        TheView = View.View()
        method = getMethod(len(params),params)    
        string_template = getTemplate(params)
        request = TheController.get(req, method, string_template)
        return TheView.getAll(req, request, params[1].lower(),root_url,params[1])
        

def index(req):
    req.content_type = 'text/html'
    req.send_http_header()
    result = []
    parameters = []
    root_url = "http://" + str(req.hostname + req.uri).replace("index.py", "")
    if str(req.args) == "None":
        result = getresult(req, None,root_url)
    else:
        parameters = getParams(req)
        for i in range(len(parameters)):
            parameters[i] = parameters[i].replace("%20"," ")
            parameters[i] = parameters[i].replace("%21","!")
            parameters[i] = parameters[i].replace("+"," ") 
        result = getresult(req, parameters,root_url)      
    return result
 