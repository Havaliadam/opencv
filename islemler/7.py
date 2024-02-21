import cv2
import numpy as np
img=cv2.imread("opencv.png")

gri=cv2.cvtColor(img,cv2.COLOR_BGR2BGR565)
gri=np.float32(gri)
corner=cv2.goodFeaturesToTrack(gri,90,0.01,10)

corner=np.int0(corner)

for c in corner:
    x,y=c.ravel()
    
    cv2.circle(img,(x,y),5,(255,0,0),-1)
    

cv2.imshow("ucgen",img)
cv2.waitKey(0)


cv2.destroyAllWindows()
