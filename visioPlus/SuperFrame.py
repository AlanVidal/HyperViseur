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
            self.faces.append(FaceFrame(frame, self.getData()[i], self.coef))

class FaceFrame(SuperFrame):

        def __init__(self,aframe, emplacement, coef):
            SuperFrame.__init__(self,aframe, coef)
            self.emplacement = emplacement
            self.eyes = []
    
        def analyseEyes(self,tools,aCoef, aNumb):
            self.data = tools.detectSomeThings(self, tools.eye_cascade,aCoef,aNumb)            

            if len(self.data) == 2 :
                i = 0
                for eye in tools.extractPartsPicture(self,self.frame):
                    print(self.coef)
                    f = lambda x,y :[ int( (x[0]*self.coef+y[0]) ) ,int( (x[1]*self.coef+y[1]) ),int(x[2]*self.coef),int(x[3]*self.coef)] 
                    newEmplacement = f(self.getData()[i], self.emplacement) #Permet de recalculer l'emplacement et la taille sur l'image d'origine.
                    self.eyes.append(EyeFrame(eye, newEmplacement, self.coef))
                    i = i + 1
            else :
                print(str(len(self.data)))

        def getEyes(self):
            return self.eyes

class EyeFrame(SuperFrame):
        def __init__(self,aframe, emplacement, coef):
            SuperFrame.__init__(self,aframe, coef)
            self.emplacement = emplacement
            self.data.append(emplacement)
            
    #A completer 