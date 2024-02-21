import cv2 
img=cv2.imread("volvo.jpg")
img=cv2.resize(img,(400,300))
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
# print(img)
cv2.imshow("image",img)#pencere açılır
cv2.imwrite("copy.jpg",img)

cv2.waitKey(0)

cv2.destroyAllWindows()
