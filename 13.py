import cv2

vid = cv2.VideoCapture("C:\\Users\\Arulmani\\OneDrive\\Videos\\Naruto.mp4")

while vid.isOpened():
    _,frame = vid.read()
    frame = cv2.resize(frame, (600, 350))

    cv2.imshow("Original", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()