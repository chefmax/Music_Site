'''
Created on 17.01.2013

@author: chef
'''
import sys
sys.path.append("/home/chef/workspace/Music_Site/src")
import re
from Views.AbstractView import AbstractView

class BandView(AbstractView):
    @classmethod  
    def getView(cls):
        if cls.View == None:
            cls.View = BandView()
        return cls.View  
    
    
    def get(self, req, rows ,method , header): 
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
                for columsIterator in colums:
                    if columnNumber == 1:
                        firstArgument = self.getTypeOfSample(req,header[0])  # band , tracks or albums 
                        toBeInserted += "       <td> " + "<a href = \"http://www.maxmusicsite.com/"  + firstArgument + "/"  + str(columsIterator).replace("'","")[0] + "/" + str(columsIterator).replace("'","") +  "\"" +">"  + str(columsIterator).replace("'","") +  "</a>"+ "  </td>" + "\n"
                        columnNumber = 2
                    else:
                        toBeInserted += "       <td> "  + str(columsIterator).replace("'","") +   " </td>" + "\n"

                toBeInserted += "  </tr>" + "\n"    
            toBeInserted += "  </tbody>" + "\n" + "</table>" + "\n"
            return toBeInserted
        