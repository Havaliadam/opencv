import cv2 
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

dosyadi="C:/Users/Acer/OneDrive/Masaüstü/OPENCV/video/ders.mp4"
codec=cv2.VideoWriter.fourcc('W','M','V','2')
framerate=30
resolution=(640,480)


output=cv2.VideoWriter(dosyadi,codec,framerate,resolution)
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    output.write(frame)
    
    cv2.imshow("webcab",frame)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
    cv2.waitKey(30)
    
output.release()    
cap.release()    
cv2.destroyAllWindows()
    


