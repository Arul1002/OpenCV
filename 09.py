import cv2

img = cv2.imread('C:\\Users\\Arulmani\\OneDrive\\Pictures\\Naruto.jpg')

ksize = (5, 5)
sigmax = 0
sigmay = 0

blur = cv2.GaussianBlur(img, ksize, sigmax, sigmay)
cv2.imshow("Original", img)
cv2.imshow("Gaussian Blur", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()