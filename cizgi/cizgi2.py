import cv2 

import numpy as np 
cap=cv2.VideoCapture("yol2.mp4")

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(400,600))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    alt=np.array([18,94,140],np.uint8)
    ust=np.array([18,94,140],np.uint8)


    mask=cv2.inRange(hsv,alt,ust)
    kenar=cv2.Canny(mask,75,250)
    cizgi=cv2.HoughLinesP(kenar,1,np.pi*180,50,maxLineGap=5)


    for i in cizgi:
        x1,y1,x2,y2=i[0]
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)



    cv2.imshow("a",mask)

    if ret==0:
        break

    if cv2.waitKey(30)& 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

