import cv2
import numpy as np

lower = np.array([15,150,20])
upper = np.array([35,255,255])

video = cv2.VideoCapture(0)

while True:
    success, img = video.read()
    image = cv2.cvtColour(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, lower, upper)

    cv2.imshow("mask",mask)
    cv2.imshow("webcam", img)

    cv2.waitkey(1)
