import os
import sys
import cv2
import numpy as np
from cgitb import text
from cmath import rect

DEFAULT_FRONTAL_FACE_CLASSIFIER = './haarcascades/haarcascade_frontalface_default.xml'

    
def main(face_cascade):
    face_cascade = cv2.CascadeClassifier(face_cascade)

    video_capture = cv2.VideoCapture(0)

    while True:
        _, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces_data = face_cascade.detectMultiScale(frame, 1.3, 5)

        if len(faces_data) > 2: # Tempo
            cv2.imwrite("./Gray_Image.jpg", gray)

        # Draw a rectangle around the faces
        i = 0;
        for (x, y, w, h) in faces_data: #Liste des visages
            cv2.rectangle(img=frame,
                          pt1=(x, y),
                          pt2=(x + w, y + h),
                          color=(255, 0, 0),
                          thickness=2)
            frame0 = frame[y - 10:y + h + 10, x - 10:x + w + 10]   
            cv2.imwrite("./Gray_Image" + str(i) + ".jpg", frame0)   #Svg des visages, verifier si deja enregistrés
            i = i + 1  

        cv2.imshow('Face Detection using a webcam ', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main('./haarcascades/haarcascade_frontalface_default.xml')
