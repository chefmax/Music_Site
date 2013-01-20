'''
Created on 17.01.2013

@author: chef
'''
import sys
from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)))
import re
from Views.AbstractView import AbstractView
import sqlite3
class View(AbstractView):
    
    def writeLetters (self, connection, cursor, typeOfLink, LevelsUp):
        if typeOfLink == "albumsbyletter":
            BandsOrAlbums = "Albums"
        else:
            BandsOrAlbums = "Bands"  
        cursor.execute("SELECT distinct substr(Description,1,1) FROM %s group by Description order by Description" % (BandsOrAlbums) )
        FirstLetters = []
        result = ""
        for i in cursor:
            resultToString = str(i)
            FirstLetters.append(resultToString[3:len(resultToString)-3])
        for i in FirstLetters :
            result += "<a href=\"" + LevelsUp + BandsOrAlbums + "> " + i +" </a> &nbsp;"
        return result    
    
    
    
    @classmethod  
    def getView(cls):
        if cls.View == None:
            cls.View = View()
        return cls.View  

            
        
    
    
    def get(self, req, rows ,typeOfLink , header, NumberOfLevels ): 
        toBeInserted = ""
        rowsNumber = len(rows)
        if rowsNumber == 0:
            return ""
        else:
            if typeOfLink == "albumsbyletter" or typeOfLink == "bandsbyletter":
                return  self.generateLetters(1, typeOfLink, rows)
            toBeInserted += "<table border = \"1px\">" + "\n" + "  <thead>"  + "\n" + "      <tr>" + "\n"
            for i in range(len(header)):
                toBeInserted += "          <th>" + str(header[i]) + "</th>"  + "\n"
            toBeInserted += "      </tr>" + "\n" + "  </thead>"  + "\n" + "  <tbody>" + "\n"
            r = re.compile("(?:')[^']+(?:')|\d+")
            for rowsIterator in rows:
                colums = r.findall(str(rowsIterator))
                toBeInserted += "    <tr>" + "\n"
                columnNumber = 1
                Arguments = ""
                for i in range(NumberOfLevels):
                    Arguments += pardir
                    Arguments += sep                       
                for columsIterator in colums:
                    if columnNumber == 1:
                        firstArgument = self.getTypeOfSample(req,header[0])  # band , tracks or albums 
                        if typeOfLink == "tracks" and len(header)>1 and header[1] == "Format":
                            toBeInserted += "       <td> " + "<a href = \"../../../download\" >"   + str(columsIterator).replace("'","") +  "</a>"+ "  </td>" + "\n"
                        else:
                            toBeInserted += "       <td> " + "<a href = \"" + Arguments  + firstArgument + "/"  + str(columsIterator).replace("'","")[0] + "/" + str(columsIterator).replace("'","") +  "\"" +">"  + str(columsIterator).replace("'","") +  "</a>"+ "  </td>" + "\n"
                    elif columnNumber == 2 and header[1] == "Owner":
                        toBeInserted += "       <td> " + "<a href = \"" + "../../../" + "bands" +  "/"  + str(columsIterator).replace("'","")[0] + "/" + str(columsIterator).replace("'","") +  "\"" +">"  + str(columsIterator).replace("'","") +  "</a>"+ "  </td>" + "\n"
                    else:
                        toBeInserted += "       <td> "  + str(columsIterator).replace("'","") +   " </td>" + "\n"
                    columnNumber += 1    
                toBeInserted += "  </tr>" + "\n"    
            toBeInserted += "  </tbody>" + "\n" + "</table>" + "\n"
            return toBeInserted