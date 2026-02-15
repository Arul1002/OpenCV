import cv2

vid = cv2.VideoCapture("C:\\Users\\Arulmani\\OneDrive\\Videos\\Naruto.mp4")

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

output = cv2.VideoWriter("C:\\Users\\Arulmani\\OneDrive\\Videos\\Screen Recordings\\"\
    "output.mp4", fourcc, 25, (600, 350))

while vid.isOpened():
    ret,frame = vid.read()
    if ret:
        output.write(frame)
        cv2.imshow("Original", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cv2.destroyAllWindows()