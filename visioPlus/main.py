#Creer une interface pour interagire avec les objets SuperFrame

import os
import sys
import cv2
import numpy as np
from cgitb import text
from cmath import rect
from SuperFrame import SuperFrame
from Tools import Tools

DEFAULT_FRONTAL_Nose_CLASSIFIER = './haarcascades/Nariz.xml'


def showPicts(name,frames): #Permet d'afficher un enssemble d'image
    i = 0
    for(frame) in frames:
            cv2.imshow(name + str(i), frame.getFrame())
            i = i+1

def main():

    video_capture = cv2.VideoCapture(0)
    tools = Tools()

    while True:
        _, originalFrame = video_capture.read()
        _, frameWitRect =  video_capture.read()

        visage = SuperFrame(frameWitRect, 1)

        grayFace = visage
        grayFace.setFrame(tools.FrameReWrite(visage))

        grayFace.setData(tools.detectSomeThings(grayFace,tools.face_cascade,1.1,4))
        grayFace.setFaces(tools.extractPartsPicture(grayFace,originalFrame))

        tools.drowRect(grayFace,frameWitRect)
        test = grayFace.getFaces()
        for face in test:
            face.analyseEyes(tools,1.3,3)
            showPicts("Eye",face.getEyes())
            for eye in face.getEyes():
                tools.drowRect(eye, frameWitRect)
        
        showPicts("d",grayFace.getFaces())
        cv2.imshow("sdd", grayFace.frame)
        cv2.imshow("f", frameWitRect)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

