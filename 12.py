import cv2
import numpy as np

img = cv2.imread('C:\\Users\\Arulmani\\OneDrive\\Pictures\\Naruto.jpg',0)
min_thresh = 100
max_thresh = 200
edge = cv2.Canny(img, min_thresh, max_thresh)
cv2.imshow("Original", img)
cv2.imshow("Canny Edge", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
