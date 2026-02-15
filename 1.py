import cv2

img = cv2.imread('C:\\Users\\Arulmani\\OneDrive\\Pictures\\Naruto.jpg',0)

print("Dimension",img.shape)

width = img.shape[1]
height = 400
dim = (width,height)
resize = cv2.resize(img, dim)

cv2.imshow("window",resize)

cv2.imwrite('leaf.jpg',img)

cv2.waitKey(0)

cv2.destroyAllWindows()