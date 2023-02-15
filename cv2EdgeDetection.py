import cv2
 
img = cv2.imread("D:/Python/openCV/Contour-Detection-using-OpenCV/edge_detection/test01.jpg") 

""" cv2.imshow('Original', img)
cv2.waitKey(0) """
 
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', img_gray)
# cv2.waitKey(0)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
# cv2.imshow('blur', img_blur)
# cv2.waitKey(0)

img_blur2 = cv2.GaussianBlur(img_gray, (15,15), 0) 
""" cv2.imshow('blur2', img_blur2)
cv2.waitKey(0) """
 
""" sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) 
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) 

cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)
cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)
cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
cv2.waitKey(0)"""

canny = cv2.Canny(image=img_blur, threshold1=50, threshold2=100) 
cv2.imshow('Canny Edge Detection', canny)
cv2.waitKey(0)
 
canny2 = cv2.Canny(image=img_blur, threshold1=150, threshold2=250) 
cv2.imshow('Canny Edge Detection2', canny2)
cv2.waitKey(0) 
 
laplacian = cv2.Laplacian(img_blur,3,cv2.CV_64F)
cv2.imshow('Laplacian', laplacian)
cv2.waitKey(0) 

cv2.destroyAllWindows()