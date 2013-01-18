'''
Created on 15.01.2013

@author: chef
'''
import sys 
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))


class AbstractView(object):
    
    View = None
    TitleIsGenerated = False
    
    @classmethod
    def getView(cls):pass
      
        
    
    def get(self, req, parameter ,typeOfLink , header ): pass
    
    
    def getTypeOfSample(self,req,parameter):
        if parameter == "Track_Name":
            return "tracks"
        elif parameter == "Band_Name":
            return "bands"
        else:
            return "albums"
    
    def getAll(self, req, parameter ,typeOfLink ):
        toBeInserted = ""
        if parameter == None:
            return self.getresult(toBeInserted)
        DivIsFirst = True
        for i in range(0,len(parameter),2):
            if DivIsFirst == True:
                toBeInserted += "<div class = \"title\" id = \"t\" >" +  "\n" + self.get(req, parameter[i] , typeOfLink, parameter[i+1]) + "</div>" + "\n"
                DivIsFirst = False
            else:
                toBeInserted += "<div class = \"title\"  >" + "\n" + self.get(req, parameter[i] ,typeOfLink , parameter[i+1]) + "</div>" + "\n"    
        return self.getresult(toBeInserted)
    
    def getresult(self,toBeInserted):
        f = open("/home/chef/workspace/title/title.html","r+")
        result = f.read()
        result = result.replace("****",toBeInserted)
        return result
    