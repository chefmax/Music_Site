'''
Created on 15.01.2013

@author: chef
'''
import sys 
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
import re


class AbstractView(object):
    
    View = None
    NumberOfLevels = 0
    LevelsUp = ""
    
    @classmethod
    def getView(cls):pass
      
        
    
    def get(self, req, parameter ,typeOfLink , header): pass
    
    def getParams(self,req):
        unparsed_parameters = "".join(req.args)
        template = re.compile("[^?&\/=]+")            
        return  template.findall(unparsed_parameters)
    
    
        
    def generateLetters(self,typeOfLink,rows):
        toBeInserted = ""    
        if typeOfLink == "albumsbyletter":
            BandsOrAlbums = "Albums"
        else:
            BandsOrAlbums = "Bands"
        for j in range(self.NumberOfLevels):
             self.LevelsUp += pardir
             self.LevelsUp += sep
        for i in rows:
            toBeInserted += "<a href = \""+ self.LevelsUp + BandsOrAlbums + "/" + str(i)[3:len(str(i))-3].replace("'", "") + "\"" + ">" +str(i)[3:len(str(i))-3].replace("'", "") + "</a>  &nbsp;"     
        return toBeInserted  
    
    
    
    
    def getHeader(self,result):
        header = result[len(result)-1]
        result.pop()
        return header

    
    def getTypeOfSample(self,req,parameter):
        if parameter == "Track_Name":
            return "tracks"
        elif parameter == "Band_Name":
            return "bands"
        else:
            return "albums"
    
    def getAll(self, req, parameter ,typeOfLink, NumberOfLevels ):
        self.NumberOfLevels = NumberOfLevels
        toBeInserted = ""
        
        for j in range(self.NumberOfLevels):
             self.LevelsUp += pardir
             self.LevelsUp += sep
        
        if parameter == None:
            return self.getresult("Root", "article section h2 number 1" ,"","****")
        title = self.getHeader(parameter)
        if typeOfLink.lower() == "albumsbyletter" or typeOfLink.lower() == "bandsbyletter":
            return self.getresult(title, "article section h2 number 1", self.generateLetters( typeOfLink, parameter[0]), "****")
        DivIsFirst = "id = \"first\" "
        toBeInserted += "<div class = \"outer\">"
        toBeInserted += "\n"
        for i in range(0,len(parameter),2):
                if (i+3) > len(parameter):
                    toBeInserted += "<div class = \"oneblock\"" +" >" +  "\n" + self.get(req, parameter[i] , typeOfLink, parameter[i+1]) + "</div>" + "\n"
                    DivIsFirst = ""
                else:
                    toBeInserted += "<div class = \"title\" "  + DivIsFirst + ">" + "\n" + self.get(req, parameter[i] ,typeOfLink , parameter[i+1]) + "</div>" + "\n" 
                    DivIsFirst = ""
        toBeInserted += "<div class = \"outer\">"
        toBeInserted += "\n" 
        return self.getresult(title,"article section h2 number 1",toBeInserted,"****")
    
    def getresult(self,toBeInsertedHead,whatReplaceHead,toBeInserted,whatReplace):
        f = open("/home/chef/workspace/Music_Site/index.html", "r+")
        result = f.read()
        result = result.replace("css/style.css",self.LevelsUp + "css/style.css")
        result = result.replace("js/libs/modernizr-2.0.6.min.js",self.LevelsUp + "js/libs/modernizr-2.0.6.min.js")
        result = result.replace("Main*",self.LevelsUp)        
        result = result.replace("Albums*",self.LevelsUp + "albumsbyletter")
        result = result.replace("Bands*",self.LevelsUp + "bandsbyletter")
        result = result.replace(whatReplaceHead,toBeInsertedHead)
        result = result.replace(whatReplace,toBeInserted)
        result = result.replace("article section h2 #2","")
        result = result.replace("article footer h3","")
        result = result.replace("#####","")
        return result
    