import cv2 
cap=cv2.VideoCapture("video.mp4")

while True:
    ret,frame=cap.read()
    
    
    if ret==0:
        break
    frame=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    
    
    cv2.imshow("video",frame)
    
    if cv2.waitKey(30)& 0xff==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()    
    
    