class SuperFrame:

    def __init__(self,aframe, emplacement, coef):
        self.frame = aframe
        self.emplacement = emplacement
        self.coef = coef
        self.data = []
        self.enssemble = []


    def getFrame(self):
        return self.frame

    def getEmplacement(self):
        return self.emplacement

    def getCoef(self):
        return self.coef

    def getReduceCoef(self):
        return 1/self.coef

    def setFrame(self,aFrame):
        self.frame = aFrame        

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getEnssemble(self):
        return self.enssemble

    def setEnssemble(self,enssemble):
        self.enssemble = enssemble

        