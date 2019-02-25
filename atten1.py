# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 00:03:51 2019

@author: kartik
"""


import cv2
import numpy as np
import os
import sqlite3

faceDetector = cv2.CascadeClassifier("C:\\Users\\kartik\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml");
name=input("enter your name")
roll=input("enter your roll num")
conn=sqlite3.connect("f.db")
p=(name, roll)
cursor=conn.execute("INSERT INTO attendace VALUES (?, ?, NULL)", p)

conn.commit()

os.mkdir('D://PROG//dataset//{}'.format(name))
k=0
cap = cv2.VideoCapture(0);

while(True):
    _, frame = cap.read();
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(gray, 1.2, 5)
    for(x, y, w, h) in faces:
      cv2.imwrite('D://PROG//dataset//{}//{}.jpg'.format(name,k),image)
      k +=1
      cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    print (len(faces))
    cv2.imshow("Face", frame)
    if(cv2.waitKey(1)== ord('q')):
      break
 
cap.release()
cv2.destroyAllWindows()