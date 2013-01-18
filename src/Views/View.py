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
    
    def writeLetters (self, connection, cursor, BandOrAlbum,file):
        cursor.execute("SELECT distinct substr(Description,1,1) FROM %s group by Description order by Description" % (BandOrAlbum) )
        FirstLetters = []
        for i in cursor:
            resultToString = str(i)
            FirstLetters.append(resultToString[3:len(resultToString)-3])
        for i in FirstLetters :
            file.write("<a href=\"http://93.175.7.147/%s/%s\"> %s </a> &nbsp;""" % (BandOrAlbum.lower(),i.lower(),i.lower()))
    
    def generateTitle(self):
        if self.TitleIsGenerated == False: 
            title = open("/home/chef/workspace/title/title.html", "r+")
            title.write("<html>" + "\n" + "<head>" + "\n" + "<link type=\"text/css\" rel=\"stylesheet\" href=\"stylesheetcss\"/>" + "</head>" + "\n")
            title.write("<h3> <a href = \"http://93.175.7.147/bands\" >" + "Bands"  + "</a> </h3>" + "\n")
            connection = sqlite3.connect('/home/chef/workspace/www/Band.db')
            cursor = connection.cursor()
            self.writeLetters(connection,cursor,"Bands",title)
           
            title.write("<h3> <a href = \"http://93.175.7.147/albums\" >" + "Albums"  + "</a> </h3>" + "\n")    
            self.writeLetters(connection,cursor,"Albums",title)
            title.write("\n " + "<br> ****" + "</html>" + "\n") 
            self.TitleIsGenerated = True   
        return 1  
    
    
    
    
    @classmethod  
    def getView(cls):
        if cls.View == None:
            cls.View = View()
        return cls.View  
    
    
    def get(self, req, rows ,typeOfLink , header ): 
        toBeInserted = ""
        rowsNumber = len(rows)
        if rowsNumber == 0:
            return ""
        else:
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
                for columsIterator in colums:
                    if columnNumber == 1:
                        firstArgument = self.getTypeOfSample(req,header[0])  # band , tracks or albums 
                        if typeOfLink == "tracks":
                            toBeInserted += "       <td> " + "<a href = \"http://93.175.7.147/download\" >"   + str(columsIterator).replace("'","") +  "</a>"+ "  </td>" + "\n"
                        else:
                            toBeInserted += "       <td> " + "<a href = \"http://93.175.7.147/"  + firstArgument + "/"  + str(columsIterator).replace("'","")[0] + "/" + str(columsIterator).replace("'","") +  "\"" +">"  + str(columsIterator).replace("'","") +  "</a>"+ "  </td>" + "\n"
                        columnNumber = 2
                    else:
                        toBeInserted += "       <td> "  + str(columsIterator).replace("'","") +   " </td>" + "\n"

                toBeInserted += "  </tr>" + "\n"    
            toBeInserted += "  </tbody>" + "\n" + "</table>" + "\n"
            return toBeInserted