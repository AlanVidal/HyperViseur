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
        data = aCascade.detectMultiScale(aSuperFrame, aCoef, aNumb)
        return data


    def extractPartsPicture2(self,aList,originalFrame, coef): #A partir d'enssemble de coordonnées, renvois un enssemble de frame
        tab = []
        for (x, y, w, h) in aList:
                print(aList)
                tab.append(originalFrame.getFrame()[int(y/coef):int(y/coef) + int(h/coef), int(x/coef):int(x/coef )+ int(w/coef)])
        return tab
        
    def detectSomeThingsAndCapt(self,aSuperFrame,aCascade, aCoef, aNumb, originalFrame):  #Renvoi un tableau correspondant a ce qui est recherché dans la cascade
        data = aCascade.detectMultiScale(aSuperFrame.getFrame(), aCoef, aNumb)
        return [self.extractPartsPicture2(data, originalFrame,aSuperFrame.getReduceCoef() ),data, originalFrame.getCoef()] #Retravailler toute cette partie !!!!!!


    def drowRect(self,list, frameAmodif): # A modifier
        for (x, y, w, h) in list:
            cv2.rectangle(img=frameAmodif, 
                pt1=(x, y),
                pt2=(x + w, y + h),
                color=(255, 255, 245),
                thickness=2)