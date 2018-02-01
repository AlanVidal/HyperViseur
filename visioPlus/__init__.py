import os
import sys
import cv2
import numpy as np
from cgitb import text
from cmath import rect
DEFAULT_FRONTAL_FACE_CLASSIFIER = './haarcascades/haarcascade_frontalface_default.xml'
DEFAULT_FRONTAL_EYE_CLASSIFIER = './haarcascades/haarcascade_eye.xml'


    
def main(face_cascade, eye_cascade):
    face_cascade = cv2.CascadeClassifier(face_cascade)
    eye_cascade = cv2.CascadeClassifier(eye_cascade)

    video_capture = cv2.VideoCapture(0)
    video_capture.set(cv2.CAP_PROP_FPS, 5)


    while True:
        _, frame = video_capture.read()
        _, frameWitRect =  video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_resized=cv2.resize(gray,(0,0),fx=0.5,fy=0.5) #Plus petit plus eco
        faces_data = face_cascade.detectMultiScale(gray_resized, 1.3, 1)

        if len(faces_data) > 1: # Tempo
            cv2.imwrite("./Gray_ImageR.jpg", gray_resized)


        i = 0;
        for (x, y, w, h) in faces_data: #Liste des visages
            cv2.rectangle(img=frameWitRect,
                          pt1=(x*2, y*2),
                          pt2=(x*2 + w*2, y*2 + h*2),
                          color=(255, 0, 0),
                          thickness=2)

            faceFrame = frame[y*2 - 10:y*2 + h*2 + 10, x*2 - 10:x*2 + w*2 + 10]

            faceFrame=cv2.resize(faceFrame,(0,0),fx=1,fy=1) 
            eye_data = eye_cascade.detectMultiScale(faceFrame, 1.2, 5)
            for (x, y, w, h) in eye_data: #Liste des yeux
                cv2.rectangle(img=faceFrame, 
                            pt1=(x, y),
                            pt2=(x + w, y + h),
                            color=(255, 0, 0),
                            thickness=2)

            


            cv2.imwrite("./frame_Image" + str(i) + ".jpg", faceFrame)   #Svg des visages, verifier si deja enregistr�s
            i = i + 1  

        cv2.imshow('Face Detection using a webcam ', frameWitRect)
        cv2.imshow('Face Detection using a webcam mini ', faceFrame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(DEFAULT_FRONTAL_FACE_CLASSIFIER,DEFAULT_FRONTAL_EYE_CLASSIFIER)
