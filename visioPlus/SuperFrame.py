#Ajouter des sous classes pour les eltms du visages et adapter les fonctions du main
from Tools import *

class SuperFrame: #
    def __init__(self,aframe, coef):
        self.frame = aframe # Image 
        self.coef = coef # Coeficient de reduction par rapport a l'image d'origine
        self.data = [] # ! utlité a debatre ! Contient les données temporaire relative aux elements constituant le visage (Oeil, nez etc...)
        self.faces = [] #Liste des visages contenu dans l'image, a deplacer dans une sous classe eye.

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
        f = lambda x,y :[ int( (x[0]/self.coef+y[0]) ) ,int( (x[1]/self.coef+y[1]) ),int(x[2]/self.coef),int(x[3]/self.coef)]  #Lambda temporaire

        for frame in faces[0]:
            self.faces.append(FaceFrame(frame, f(faces[1][i],[0,0,0,0]), self.coef))



    def getFacesX(self,f):
            faceLocations = []
            for face in self.faces:
                faceLocations.append(f(face))
            return faceLocations

    def getFaceFrame(self):
        return self.getFacesX(lambda x: x.getFrame())

    def getFacesLocations(self):
        return self.getFacesX( lambda x: x.getEmplacement())

class FaceFrame(SuperFrame):
        def __init__(self,aframe, emplacement, coef):
            SuperFrame.__init__(self,aframe, coef)
            self.emplacement = emplacement
            self.eyes = []
    
        def analyseEyes(self,tools,aCoef, aNumb,originalFrame):
            data =  tools.detectSomeThingsAndCapt(self,tools.eye_cascade,1.1,3,originalFrame)           
            print(str(originalFrame.getCoef() ))

            if (len(data[0])) > 0 :
                i = 0
                for eye in data[1]:
                    f = lambda x,y :[ int( (x[0]+y[0]) ) ,int( (x[1]+y[1]) ),int(x[2]),int(x[3])] 
                    newEmplacement = f(data[1][i], self.emplacement) #Permet de recalculer l'emplacement et la taille sur l'image d'origine.
                    self.eyes.append(EyeFrame(data[0][i], newEmplacement,  originalFrame.getCoef()))
                    i = i + 1
            else :
                print(str(len(self.data)))

        def getEyes(self):
            return self.eyes

        def getEyesLocations(self):
            eyesLocations = []
            for eye in self.eyes:
                eyesLocations.append(eye.getEmplacement())
            return eyesLocations




class EyeFrame(SuperFrame):
        def __init__(self,aframe, emplacement, coef):
            SuperFrame.__init__(self,aframe, coef)
            self.emplacement = emplacement
            self.data.append(emplacement) #Simplifie poour l'affichage, a enlever si analyse a l'interieur de l'oeil
            
    #A completer 