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
        
        def getController(self,kind_of_controller):
               if kind_of_controller.lower() == "albums":
                         return AlbumController.AlbumController
               elif kind_of_controller.lower() == "bands":
                         return BandController.BandController
               elif kind_of_controller.lower() == "tracks":
                         return TrackController.TrackController
               elif kind_of_controller.lower() == "js" or kind_of_controller.lower() == "css":
                   return  CssJsController.CssJsController() 
               elif kind_of_controller.lower() == "band_img":
                   return  BandImgController.BandImgController
               else:
                   raise Exception
        
        
        
        def getParams(self):
            unparsed_parameters = str(self.path)
            if unparsed_parameters == "/":
                return "None"
            elif  unparsed_parameters.find('?') > -1:
                template = re.compile('(?:[=])([^?&\/=]+)')
                return template.findall(unparsed_parameters)
            else:
                template = re.compile("[^?&\/=]+") 
                return template.findall(unparsed_parameters)   

        def getRootUrl(self):
          return "/"


        def getTemplate(self,parameters):
            method = self.getMethod(len(parameters),parameters)
            if parameters[0] == "css" or parameters[0] == "js":
                return dirname(realpath(__file__)) + self.path
            elif method == "get":
                return parameters[len(parameters)-1]
            elif method == "getAllByLetter":
                  return parameters[len(parameters)-1]
            elif parameters[0] == "band_img":
                  return parameters[len(parameters)-1]
            else:      
                   return None


        def getMethod(self,numberOfParameters,parameters):
	           if numberOfParameters == 1:
		              return "getAll"
	           elif numberOfParameters == 2:
		              return "getAllByLetter"
	           else:
		              return "get"


        def getresult(self,params,root_url):  
    	    if params == None:
    		      return RootView.RootView.getAll(None, root_url, None)
    	    else:
    		      TheController = self.getController(params[0])
    		      method = self.getMethod(len(params),params)    
    		      string_template = self.getTemplate(params)
            return TheController.get(method,string_template,root_url)
        
        def get_response(self):
            parameters = self.getParams()
            self.typeContent = "text/html"
            if parameters != "None":
                for i in range(len(parameters)):
                    parameters[i] = parameters[i].replace("%20",u" ")
                    parameters[i] = parameters[i].replace("%21",u"!")
                    parameters[i] = parameters[i].replace("+",u" ") 
                if parameters[0] == "css":
                        self.typeContent = "text/css"
                elif parameters[0] == "js":
                        self.typeContent = "text/javascript"
                elif parameters[0] == "band_img":
                    self.typeContent = "image/*"        
                return self.getresult(parameters,self.getRootUrl()) 
            else:   
                return self.getresult(None,self.getRootUrl()) 
        
        
        def do_GET(self):
           self.send_response(200)
           root_url = self.getRootUrl()
           
           request = self.get_response()
           if self.typeContent == "text/css" or self.typeContent == "text/javascript":
               self.send_header("Content-type", self.typeContent)   
               self.end_headers() 
               for i in request:
                   self.wfile.write(i)
           elif self.typeContent == "image/*":
               self.send_header("Content-type", self.typeContent)               
               self.end_headers()          
               self.wfile.write(request)
                       
           else:   
               self.send_header("Content-type", "text/html")               
               self.send_header("Content-length", len(request.encode("utf-8")))
               self.end_headers()          
               self.wfile.write(request.encode("utf-8"))



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
