import cv2 
import numpy as np 

img=cv2.imread("volvo.jpg")

img[200,300,0]=0
print(img[200,300])


beyaz=img.item(150,150,0)
print(beyaz
      )
img.itemset((150,150,0),200)
print(img[150,150])




"""
renk=img[200,300,0]
print(renk)
#print(img.shape)#renk katmanını gçsterir boyut

gri=img[200,300,0]
print("gri",gri)
beyaz=img[200,300,1]
print("beyaz",beyaz)
kirmizi=img[200,300,0]
print("kirmizi:",kirmizi)
"""
cv2.imshow("araba",img)

cv2.waitKey(0)
cv2.destroyAllWindows()




