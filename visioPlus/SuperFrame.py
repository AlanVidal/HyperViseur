#Ajouter des sous classes pour les eltms du visages et adapter les fonctions du main
class SuperFrame:

    def __init__(self,aframe, emplacement, coef):
        self.frame = aframe
        self.emplacement = emplacement
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
        print(1/self.coef)
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
        for frame in faces:
            self.faces.append(FaceFrame(frame, 0, self.coef))

class FaceFrame(SuperFrame):
        def __init__(self,aframe, emplacement, coef):
            SuperFrame.__init__(self,aframe, emplacement, coef)
            self.eyes = []

        def setEyes(eyes):
            self.eyes = eyes