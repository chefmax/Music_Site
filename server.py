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
from Models import *
from Views import *
import socket
import urllib2



class ThreadingSimpleServer(SocketServer.ThreadingMixIn,BaseHTTPServer.HTTPServer):
    pass

class MusicSiteHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	"""docstring for MusicSiteHandler"""
        ip = None
        typeContent = "text/html"
        kinds = ["bands","albums","tracks"]
        
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
          return "http://" + str(self.getIp()) + ":8000/"
        
        
        def getController(self,kind_of_controller):
	           if kind_of_controller.lower() == "albums":
		                 return AlbumController.AlbumController.getController()
	           elif kind_of_controller.lower() == "bands":
		                 return BandController.BandController.getController()
	           elif kind_of_controller.lower() == "tracks":
		                 return TrackController.TrackController.getController()
        
        def getIp(self):
            if self.ip == None:
                return urllib2.urlopen('http://ip.42.pl/raw').read()
            else:
                return self.ip




        def getMethod(self,numberOfParameters,parameters):
	           if numberOfParameters == 1:
		              return "getAll"
	           elif numberOfParameters == 2:
		              return "getAllByLetter"
	           else:
		              return "get"

        def getTemplate(self,parameters):
	    method = self.getMethod(len(parameters),parameters)
    	    if method == "get":
                return parameters[2]
    	    elif method == "getAllByLetter":
    		      return parameters[len(parameters)-1]
    	    else:
    	           return None


        def getLevel(self,params):
    	    if params[len(params)-2] == "num":
                return int(params[len(params)-1])
    	    else:
    	        return len(params)/2

        def getresult(self,params,root_url):  
    	    if str(params) == "None" or params[0]  not in self.kinds:
    		      TheView = View.View()
    		      return TheView.getAll(self,None,None,root_url,None)
    	    else:
    		      TheController = self.getController(params[0])
    		      TheView = View.View()
    		      method = self.getMethod(len(params),params)    
    		      string_template = self.getTemplate(params)
    		      request = TheController.get(self, method, string_template)
    		      return TheView.getAll(self, request, params[0].lower(),root_url,params[0])
    		
        def get_response(self):
            parameters = self.getParams()
            self.typeContent = "text/html"
            if parameters != "None":
                for i in range(len(parameters)):
                    parameters[i] = parameters[i].replace("%20",u" ")
                    parameters[i] = parameters[i].replace("%21",u"!")
                    parameters[i] = parameters[i].replace("+",u" ") 
                if parameters[0] == "css" or parameters[0] == "js" :
                    if parameters[0] == "css":
                        self.typeContent = "text/css"
                        path = "css/"
                    else:
                        self.typeContent = "text/javascript"
                        path = "js/libs/"
                    file = parameters[len(parameters)-1]    
                    source = open(path + file,"r+")
                    result = source.readlines()   
                    source.close()
                    return result
                else:
                    return self.getresult(parameters,self.getRootUrl()) 
            else:   
                return self.getresult("None",self.getRootUrl()) 
        
        
        def do_GET(self):
           self.send_response(200)
           root_url = self.getRootUrl()
           
           request = self.get_response()
           if self.typeContent == "text/css" or self.typeContent == "text/javascript":
               if self.typeContent == "text/css":
                   self.send_header("Content-type", "text/css")
               else:
                   self.send_header("Content-type", "text/javascript")   
               self.end_headers() 
               for i in request:
                   self.wfile.write(i)
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
