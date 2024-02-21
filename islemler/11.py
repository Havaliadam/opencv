import cv2 
import numpy as np 
img1=cv2.imread("u1.png")

gri=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ai,thresh=cv2.threshold(gri,100,200,cv2.THRESH_BINARY)
m=cv2.moments(thresh)
print(m)
x=int(m["m10"]/m["m00"])
y=int(m["m01"]/m["m00"])

cv2.circle(img1,(x,y),10,(255,0,0),-1)


cv2.imshow("u",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()