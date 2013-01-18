from mod_python import apache
import sqlite3
import time
import re
import sys
sys.path.append("/home/chef/workspace/Music_Site/src")
from Controllers import *
from Models import *
from Views import *

def getController(kind_of_controller):
    if kind_of_controller.lower() == "albums":
        return AlbumController.AlbumController.getController()
    elif kind_of_controller.lower() == "bands":
        return BandController.BandController.getController()
    else:
        return TrackController.TrackController.getController()



def getMethod(numberOfParameters):
    if numberOfParameters == 2:
        return "getAll"
    elif numberOfParameters == 4:
        return "getAllByLetter"
    else:
        return "get"

def getTemplate(parameters):
    method = getMethod(len(parameters))
    if method == "get":
        return parameters[5]
    elif method == "getAllByLetter":
        return parameters[3]
    else:
        return None


def getresult(req, params):  
    if params == None:
        TheView = View.View.getView()
        TitleIsGenerated = TheView.generateTitle()
        return TheView.getAll(req,None,None)
    else:
        TheController = getController(params[1])
        TheView = View.View.getView()
        TitleIsGenerated = TheView.generateTitle()
        method = getMethod(len(params))    
        string_template = getTemplate(params)
        request = TheController.get(req, method, string_template)
        return TheView.getAll(req, request, params[1])
        

def index(req):
    req.content_type = 'text/html'
    req.send_http_header()
    result = []
    parameters = []
    if str(req.args) == "None":
        result = getresult(req, None)
    else:
        unparsed_parameters = "".join(req.args)
        template = re.compile("[^?&\/=]+")            
        parameters = template.findall(unparsed_parameters)
        for i in range(len(parameters)):
            parameters[i] = parameters[i].replace("%20"," ")
        result = getresult(req, parameters)

    return result