import cv2 

import numpy as np 


cap=cv2.VideoCapture("yol.mp4")
sub=cv2.createBackgroundSubtractorMOG2(history=50,varThreshold=50,detectShadows=True)
while True:
    a,frame=cap.read()
    m=sub.apply(frame)
    if cv2.waitKey(20)& 0xFF==ord("q"):
         break
    cv2.imshow("frame",frame)
    cv2.imshow("mask",m)
    

cap.release()
cv2.destroyAllWindows()