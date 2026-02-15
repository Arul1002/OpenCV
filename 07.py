import cv2

img = cv2.imread('C:\\Users\\Arulmani\\OneDrive\\Pictures\\Naruto.jpg')
row = img.shape[1]
col = img.shape[0]

center = (row//2, col//2)
angle = 90

r = cv2.getRotationMatrix2D(center, angle, 1)

rotate = cv2.warpAffine(img, r, (row, col))

cv2.imshow("Original", img)
cv2.imshow("Rotated", rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()