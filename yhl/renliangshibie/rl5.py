import numpy as np
import cv2
camera = cv2.VideoCapture(0)
cv2.namedWindow('MyCamera')

while True:
    success, frame = camera.read()
    cv2.imshow('MyCamera',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyWindow('MyCamera')
camera.release()