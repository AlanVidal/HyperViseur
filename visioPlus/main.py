import os
import sys
import cv2
import numpy as np
from cgitb import text
from cmath import rect
from SuperFrame import SuperFrame

DEFAULT_FRONTAL_FACE_CLASSIFIER = './haarcascades/haarcascade_frontalface_alt2.xml'
DEFAULT_FRONTAL_EYE_CLASSIFIER = './haarcascades/haarcascade_eye.xml'
DEFAULT_FRONTAL_Nose_CLASSIFIER = './haarcascades/Nariz.xml'


def showPicts(name,frames): #Permet d'afficher un enssemble d'image
    i = 0
    for(frame) in frames:
            cv2.imshow(name + str(i), frame)
            i = i+1

def FrameReWrite(aFrame): #Modifie une image
    newFrame = cv2.cvtColor(aFrame.getFrame(),cv2.COLOR_BGR2GRAY)
    newFrame =cv2.resize(newFrame,(0,0),fx=aFrame.getReduceCoef(),fy=aFrame.getReduceCoef()) 
    return newFrame

def detectSomeThings(aFrame,aCascade, aCoef, aNumb):  #Renvoi un tableau correspondant a ce qui est recherché dans la cascade
    data = aCascade.detectMultiScale(aFrame.getFrame(), aCoef, aNumb)
    return data

def extractPartsPicture(aFrame,originalFrame): #A partir d'enssemble de coordonnées, renvois un enssemble de frame
    tab = []
    aCoef =  aFrame.getCoef()
    for (x, y, w, h) in aFrame.getData():
            tab.append(originalFrame[y*aCoef:y*aCoef + h*aCoef, x*aCoef:x*aCoef + w*aCoef])
    return tab
    
def drowRect(aFrame, frameAmodif):
    for (x, y, w, h) in aFrame.getData():
        aCoef = aFrame.getCoef()
        cv2.rectangle(img=frameAmodif, 
            pt1=(x*aCoef, y*aCoef),
            pt2=(x*aCoef + w*aCoef, y*aCoef + h*aCoef),
            color=(255, 255, 245),
            thickness=2)

def main(face_cascade, eye_cascade,nose_cascade):

    face_cascade = cv2.CascadeClassifier(face_cascade)
    eye_cascade = cv2.CascadeClassifier(eye_cascade)
    nose_cascade = cv2.CascadeClassifier(nose_cascade)
    video_capture = cv2.VideoCapture(0)

    while True:
        _, originalFrame = video_capture.read()
        _, frameWitRect =  video_capture.read()

        visage = SuperFrame(frameWitRect,0, 1 )

        grayFace = visage
        grayFace.setFrame(FrameReWrite(visage))

        grayFace.setData(detectSomeThings(grayFace,face_cascade,1.5,5))
        grayFace.setEnssemble(extractPartsPicture(grayFace,originalFrame))
        showPicts("d",grayFace.getEnssemble())
        drowRect(grayFace,frameWitRect)

        cv2.imshow("sdd", grayFace.frame)
        cv2.imshow("f", frameWitRect)



        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(DEFAULT_FRONTAL_FACE_CLASSIFIER,DEFAULT_FRONTAL_EYE_CLASSIFIER,DEFAULT_FRONTAL_Nose_CLASSIFIER)

