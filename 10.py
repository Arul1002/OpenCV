import cv2

img = cv2.imread('C:\\Users\\Arulmani\\OneDrive\\Pictures\\Naruto.jpg')

ksize = 1

blur = cv2.medianBlur(img, ksize)

cv2.imshow("Original", img)
cv2.imshow("Median Blur", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()