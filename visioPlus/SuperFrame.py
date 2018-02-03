#Ajouter des sous classes pour les eltms du visages et adapter les fonctions du main
from Tools import *

class SuperFrame:

    def __init__(self,aframe, coef):
        self.frame = aframe
        self.coef = coef
        self.data = []
        self.faces = []


    def getFrame(self):
        return self.frame

    def getEmplacement(self):
        return self.emplacement

    def getCoef(self):
        return self.coef

    def getReduceCoef(self):
        return (1/self.coef) 

    def setFrame(self,aFrame):
        self.frame = aFrame

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getFaces(self):
        return self.faces

    def setFaces(self,faces):
        i = 0
        for frame in faces:
            print(self.getData()[i])
            self.faces.append(FaceFrame(frame, self.getData()[i], self.coef))

class FaceFrame(SuperFrame):

        def __init__(self,aframe, emplacement, coef):
            SuperFrame.__init__(self,aframe, coef)
            self.emplacement = emplacement

            self.eyes = []
    
        def setEyes(self,aEyes):
            i = 0
            for eye in aEyes:
                f = lambda x,y :[x[0]+y[0],x[1]+y[1],x[2],x[3]] 
                test = f(self.getData()[i], self.emplacement)

                print("Data" + str(self.getData()[i]) + " + " + str(self.emplacement) + " " + str(test))

                self.eyes.append(EyeFrame(eye, test, self.coef))
                i = i + 1
        def analyseEyes(self,tools,aCoef, aNumb):
            self.data = tools.detectSomeThings(self, tools.eye_cascade,aCoef,aNumb)
            eyes = self.setEyes(tools.extractPartsPicture(self,self.frame))
           
            if eyes != None :
                self.setEyes(eyes)

        def getEyes(self):
            return self.eyes

class EyeFrame(SuperFrame):
        def __init__(self,aframe, emplacement, coef):
            SuperFrame.__init__(self,aframe, coef)
            print(coef)
            self.emplacement = emplacement
            self.data.append(emplacement)
            
    #A completer 