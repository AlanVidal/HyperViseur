import cv2
import numpy as np
from cgitb import text
from cmath import rect
DEFAULT_FRONTAL_FACE_CLASSIFIER = './haarcascades/haarcascade_frontalface_alt2.xml'
DEFAULT_FRONTAL_EYE_CLASSIFIER = './haarcascades/haarcascade_eye.xml'

class Tools :
    
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(DEFAULT_FRONTAL_FACE_CLASSIFIER)
        self.eye_cascade = cv2.CascadeClassifier(DEFAULT_FRONTAL_EYE_CLASSIFIER)


    def FrameReWrite(self,aSuperFrame): #Modifie une image
        newFrame = cv2.cvtColor(aSuperFrame.getFrame(),cv2.COLOR_BGR2GRAY)
        newFrame =cv2.resize(newFrame,(0,0),fx=aSuperFrame.getCoef(),fy=aSuperFrame.getCoef()) 
        return newFrame

    def detectSomeThings(self,aSuperFrame,aCascade, aCoef, aNumb):  #Renvoi un tableau correspondant a ce qui est recherché dans la cascade
        data = aCascade.detectMultiScale(aSuperFrame.getFrame(), aCoef, aNumb)
        return data

    def extractPartsPicture(self,aSuperFrame,originalFrame): #A partir d'enssemble de coordonnées, renvois un enssemble de frame
        tab = []
        aCoef =  int(aSuperFrame.getReduceCoef())
        for (x, y, w, h) in aSuperFrame.getData():
                tab.append(originalFrame[y*aCoef:y*aCoef + h*aCoef, x*aCoef:x*aCoef + w*aCoef])
        return tab
        
    def drowRect(self,aFrame, frameAmodif):
        for (x, y, w, h) in aFrame.getData():
            aCoef = int(aFrame.getReduceCoef())
            cv2.rectangle(img=frameAmodif, 
                pt1=(x*aCoef, y*aCoef),
                pt2=(x*aCoef + w*aCoef, y*aCoef + h*aCoef),
                color=(255, 255, 245),
                thickness=2)