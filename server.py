# -*- coding: utf-8 -*- 
import SocketServer
import BaseHTTPServer
import SimpleHTTPServer
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
from Views import *




class ThreadingSimpleServer(SocketServer.ThreadingMixIn,BaseHTTPServer.HTTPServer):
    pass

class MusicSiteHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	"""docstring for MusicSiteHandler"""
        typeContent = "text/html"
        controllers = {"albums":AlbumController.AlbumController,"bands":BandController.BandController,
                       "tracks":TrackController.TrackController,"js":CssJsController.CssJsController,
                       "css":CssJsController.CssJsController,"band_img":BandImgController.BandImgController}
        methods = ["getAll","getAllByLetter","get"]
        contentTypes  = {"css":"text/css","js":"text/javascript","band_img":"image/*"}
        
        def getController(self,kind_of_controller):
            if kind_of_controller in self.controllers:
                return self.controllers[kind_of_controller]
            else:
                return None
              
        def cleanParams(self,parameters):
            for i in range(len(parameters)):
                parameters[i] = parameters[i].replace("%20",u" ")
                parameters[i] = parameters[i].replace("%21",u"!")
                parameters[i] = parameters[i].replace("+",u" ") 
        
        
        def getParams(self):
            unparsed_parameters = str(self.path)
            if unparsed_parameters == "/":
                return None
            elif  unparsed_parameters.find('?') > -1:
                template = re.compile('(?:[=])([^?&\/=]+)')
                return template.findall(unparsed_parameters)
            else:
                template = re.compile("[^?&\/=]+") 
                return template.findall(unparsed_parameters)   

        def getRootUrl(self):
          return "/"


        def getTemplate(self,parameters):
            method = self.methods[len(parameters)-1]
            if parameters[0] in ["css","js"]:
                return dirname(realpath(__file__)) + self.path
            elif method in ["get","getAllByLetter","band_img"]:
                return parameters[len(parameters)-1]
            else:      
                   return None


        def getresult(self,params,root_url):  
            if params == None:
                  return RootView.RootView.getAll(None, root_url, None)
            else:
                  TheController = self.getController(params[0].lower())
                  if TheController == None:
                      return "The controller is None!"
                  method = self.methods[len(params)-1]   
                  string_template = self.getTemplate(params)
            return TheController.getRequest(method,string_template,root_url)

        
        def get_response(self):
            parameters = self.getParams()
            self.typeContent = "text/html"
            if parameters != None:
                self.cleanParams(parameters)
                if parameters[0] in self.contentTypes:
                    self.typeContent = self.contentTypes[parameters[0]]       
                return self.getresult(parameters,self.getRootUrl()) 
            else:   
                return self.getresult(None,self.getRootUrl()) 
         
        def sendRequest(self,request):
            self.send_header("Content-type", self.typeContent)   
            self.end_headers()         
            if self.typeContent == "text/css" or self.typeContent == "text/javascript":
                for i in request:
                   self.wfile.write(i)
            elif self.typeContent == "image/*":
                self.wfile.write(request)
            else:
                self.wfile.write(request.encode("utf-8"))    
                 
        
        def do_GET(self):
           self.send_response(200)
           root_url = self.getRootUrl()
           
           request = self.get_response()
           self.sendRequest(request)



if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000

server = ThreadingSimpleServer(('', port), MusicSiteHandler)
try:
    while 1:
        sys.stdout.flush()
        server.handle_request()
except KeyboardInterrupt:
    print "Finished"
