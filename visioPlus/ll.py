import os
import sys
import cv2
import numpy as np
from cgitb import text
from cmath import rect
DEFAULT_FRONTAL_FACE_CLASSIFIER = './haarcascades/haarcascade_frontalface_alt2.xml'
DEFAULT_FRONTAL_EYE_CLASSIFIER = './haarcascades/haarcascade_eye.xml'
DEFAULT_FRONTAL_Nose_CLASSIFIER = './haarcascades/Nariz.xml'


def detecSomething(aFrame,aCoef, aNumb,aCascade, resizeX,resizeY):
    frame = cv2.cvtColor(aFrame,cv2.COLOR_BGR2GRAY)
    frame =cv2.resize(aFrame,(0,0),fx=resizeX,fy=resizeY) 
    data = aCascade.detectMultiScale(frame, aCoef, aNumb)
    return data

def detecSomethingTab(frameRect,aFrame,aCoef, aNumb,aCascade, resizeX,resizeY): #Permet d'analyser un enssemble d'image 
    tableOfNewPict = []
    for (frame) in aFrame:
        data = detecSomething(frameRect,aCoef, aNumb,aCascade, resizeX,resizeY)
        tableOfNewPict.append(frameForDrow(frameRect,frame, data, 1))

    return tableOfNewPict

def frameForDrow(frameRect,originalFrame, aData, aCoef): #Renvoi des morceaux d'image
    tab = []
    for (x, y, w, h) in aData:
        tab.append(originalFrame[y*aCoef:y*aCoef + h*aCoef, x*aCoef:x*aCoef + w*aCoef])
        cv2.rectangle(img=frameRect, 
            pt1=(x*aCoef, y*aCoef),
            pt2=(x*aCoef + w*aCoef, y*aCoef + h*aCoef),
            color=(255, 255, 245),
            thickness=2)
    return tab

def showPicts(name,frames):
    i = 0
    for(frame) in frames:
            cv2.imshow(name + str(i), frame)
            i = i+1
    
    
def main(face_cascade, eye_cascade,nose_cascade):
    face_cascade = cv2.CascadeClassifier(face_cascade)
    eye_cascade = cv2.CascadeClassifier(eye_cascade)
    nose_cascade = cv2.CascadeClassifier(nose_cascade)

    video_capture = cv2.VideoCapture(0)
    

    while True:
        _, originalFrame = video_capture.read()
        _, frameWitRect =  video_capture.read()

        faceFrame = detecSomething(originalFrame,1.3,2, face_cascade,0.5,0.5)
        faceTab = frameForDrow(frameWitRect,originalFrame,faceFrame,2) # get eyes tab
        eyeFrame = detecSomethingTab(originalFrame,faceTab, 1.2,5, eye_cascade, 1,1) 
        for elmt in eyeFrame:
            showPicts("eyes",elmt)

#        noseFrame = detecSomethingTab(faceTab, 1.4,2, nose_cascade, 1,1) 
#        for elmt in noseFrame:
#                   showPicts("nose",elmt)

        showPicts("faces",faceTab)
        cv2.imshow("BIG", originalFrame)
        cv2.imshow("BIGRect", frameWitRect)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(DEFAULT_FRONTAL_FACE_CLASSIFIER,DEFAULT_FRONTAL_EYE_CLASSIFIER,DEFAULT_FRONTAL_Nose_CLASSIFIER)

