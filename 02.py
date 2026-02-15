import cv2
import numpy as np

img = cv2.imread('C:\\Users\\Arulmani\\OneDrive\\Pictures\\Naruto.jpg')

width = 600
height = 850
dim = (width,height)
resized = cv2.resize(img, dim)

kernal = np.ones((5,5), dtype = 'uint8')

#erosion = cv2.erode(resized, kernal, iterations=1)
#dilation = cv2.dilate(resized, kernal, iterations=1)
#opening = cv2.morphologyEx(resized, cv2.MORPH_OPEN, kernal)
#closing = cv2.morphologyEx(resized, cv2.MORPH_CLOSE, kernal)
#gradient = cv2.morphologyEx(resized, cv2.MORPH_GRADIENT, kernal)
tophat = cv2.morphologyEx(resized, cv2.MORPH_TOPHAT, kernal)
blackhat = cv2.morphologyEx(resized, cv2.MORPH_BLACKHAT, kernal)

cv2.imshow("Original : ",resized)
#cv2.imshow("Erosion : ",erosion)
#cv2.imshow("Dilation : ",dilation)
#cv2.imshow("Opening : ",opening)
#cv2.imshow("Closing : ",closing)
#cv2.imshow("Gradient : ",gradient)
cv2.imshow("TopHat : ",tophat)
cv2.imshow("BlackHat : ",blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()