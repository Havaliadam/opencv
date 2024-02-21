import cv2
import numpy as np 

img=cv2.imread("1.png")
img2=cv2.imread("2.jpg")
img3=cv2.imread("3.jpg")


blr=cv2.blur(img,(15,15))
gb=cv2.GaussianBlur(img,(15,15),cv2.BORDER_DEFAULT)
mb=cv2.medianBlur(img2,9)
b=cv2.bilateralFilter(img3,9,225,225)

cv2.imshow("orj",img3)
cv2.imshow("b",b)






cv2.waitKey(0)
cv2.destroyAllWindows()