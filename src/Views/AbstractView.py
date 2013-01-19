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
      
        
    
    def get(self, req, parameter ,typeOfLink , header, NumberOfLevels ): pass
    
    
    def getHeader(self,req,NumberOfLevels,LinkType,Value):
        if NumberOfLevels == 0 :
            return "Root"
        elif NumberOfLevels == 1:
            return "All " + self.getTypeOfSample(req, LinkType)
        elif NumberOfLevels == 2:
            return  "All "+ self.getTypeOfSample(req, LinkType) + " by " + "first letter" 
        else:
            return Value
    
    def getTypeOfSample(self,req,parameter):
        if parameter == "Track_Name":
            return "tracks"
        elif parameter == "Band_Name":
            return "bands"
        else:
            return "albums"
    
    def getAll(self, req, parameter ,typeOfLink, NumberOfLevels ):
        toBeInserted = ""
        title = self.getHeader(req, NumberOfLevels, typeOfLink, typeOfLink)
        if parameter == None:
            return self.getresult("",toBeInserted)
        DivIsFirst = "id = \"first\" "
        toBeInserted += "<div class = \"outer\">"
        toBeInserted += "\n"
        for i in range(0,len(parameter),2):
                if (i+3) > len(parameter):
                    toBeInserted += "<div class = \"oneblock\"" +" >" +  "\n" + self.get(req, parameter[i] , typeOfLink, parameter[i+1], NumberOfLevels) + "</div>" + "\n"
                    DivIsFirst = ""
                else:
                    toBeInserted += "<div class = \"title\" "  + DivIsFirst + ">" + "\n" + self.get(req, parameter[i] ,typeOfLink , parameter[i+1], NumberOfLevels) + "</div>" + "\n" 
                    DivIsFirst = ""
        toBeInserted += "<div class = \"outer\">"
        toBeInserted += "\n" 
        return self.getresult(title,"article section h2 number 1",toBeInserted,"****")
    
    def getresult(self,toBeInsertedHead,whatReplaceHead,toBeInserted,whatReplace):
        f = open("/home/chef/workspace/Music_Site/index.html", "r+")
        result = f.read()
        result = result.replace(whatReplaceHead,toBeInsertedHead)
        result = result.replace(whatReplace,toBeInserted)
        return result
    