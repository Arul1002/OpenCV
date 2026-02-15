import cv2

img = cv2.imread('C:\\Users\\Arulmani\\OneDrive\\Pictures\\Naruto.jpg')
width = 600
height = 350

dimension = (width, height)
resized = cv2.resize(img, dimension)

flip = cv2.flip(resized, 1)
cv2.imshow("FLipped", flip)

flip1 = cv2.flip(resized, 0)
cv2.imshow("FLipped 1", flip1)


cv2.waitKey(0)
cv2.destroyAllWindows()