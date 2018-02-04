# Creer une interface pour interagire avec les objets SuperFrame

from cgitb import text
from cmath import rect
import os
import sys
import cv2
from SuperFrame import SuperFrame
from Tools import Tools
import numpy as np


DEFAULT_FRONTAL_Nose_CLASSIFIER = './haarcascades/Nariz.xml'


def showPicts(name, frames):  # Permet d'afficher un enssemble d'image
    i = 0
    for(frame) in frames:
            cv2.imshow(name + str(i), frame)
            i = i + 1

def main():

    video_capture = cv2.VideoCapture(0)
    tools = Tools()

    while True: #Nettoyage a faire !
        _, original = video_capture.read()
        _, frameWitRect = video_capture.read()

        originalFrame = SuperFrame(original,1)
        visage = SuperFrame(frameWitRect,0.5)

        grayFace = visage
        grayFace.setFrame(tools.FrameReWrite(visage))

        #grayFace.setData(tools.detectSomeThings(grayFace, tools.face_cascade, 1.1, 3))
        #grayFace.setFaces(tools.extractPartsPicture(grayFace, originalFrame))
        
        grayFace.setFaces(tools.detectSomeThingsAndCapt(grayFace, tools.face_cascade,1.3,3,originalFrame))

        showPicts(" Face n° ) ",grayFace.getFaceFrame())

        test = grayFace.getFaces()
        tools.drowRect(grayFace.getFacesLocations(), frameWitRect)
        

        for face in test:
            face.analyseEyes(tools, 1.3, 3,originalFrame)
            showPicts("Eye n° ", [x.getFrame() for x in face.getEyes()] ) #Lambda recuperer l'image pour chaque eye dans face.
            tools.drowRect(face.getEyesLocations(),frameWitRect)

        cv2.imshow("sdd", grayFace.frame)
        cv2.imshow("f", frameWitRect)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

