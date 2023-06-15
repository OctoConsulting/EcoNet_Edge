import cv2

cap = cv2.VideoCapture('rtmp://172.25.64.1:1953')

while True:
    ret, frame = cap.read()

    if ret:
        cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()