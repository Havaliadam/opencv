import cv2 

img=cv2.imread("volvo.jpg")
roi=img[230:320,170:300]
cv2.imshow("resim",img)
cv2.imshow("roi",roi)


cv2.waitKey(0)
cv2.destroyAllWindows()