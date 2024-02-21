import cv2 
import numpy as np 


canvas=np.zeros((500,500,3),np.uint8)+255

# cv2.line(canvas,(100,100),(300,300),(0,0,255),thickness=5)
# cv2.line(canvas,(200,350),(400,500),(255,0,0),8)


cv2.rectangle(canvas,(160,160),(360,360),(0,255,0),-1)

cv2.circle(canvas,(100,100),100,(255,0,0),4)

v1=(300,400)
v2=(300,400)
v3=(500,300)

cv2.line(canvas,v1,v2,(0,0,0),4)
cv2.line(canvas,v2,v3,(0,0,0),4)
cv2.line(canvas,v1,v3,(0,0,0),4)

cv2.imshow("pencere",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()