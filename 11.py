import cv2

img = cv2.imread('C:\\Users\\Arulmani\\OneDrive\\Pictures\\Naruto.jpg')

resized = cv2.resize(img, (500, 500))

d = 7
sigmacolor = 100
sigmaspace = 100

b = cv2.bilateralFilter(resized, d, sigmacolor, sigmaspace)

cv2.imshow("Original", resized)
cv2.imshow("Bilateral Filter", b)
cv2.waitKey(0)
cv2.destroyAllWindows()