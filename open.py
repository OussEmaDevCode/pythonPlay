#Script that detects faces and draws contours around them 

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([0, 100, 100])
    upper_blue = np.array([10, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    contours,hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    try:
        hierarchy = hierarchy[0]
    except:
        hierarchy = []

    height, width = mask.shape
    min_x, min_y = width, height
    max_x = max_y = 0
    i = 0
    # computes the bounding box for the contour, and draws it on the frame,
    for contour, hier in zip(contours, hierarchy):
        (x, y, w, h) = cv2.boundingRect(contour)
        min_x, max_x = min(x, min_x), max(x + w, max_x)
        min_y, max_y = min(y, min_y), max(y + h, max_y)
        if w > 80 and h > 80:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            i = i + 1

    if max_x - min_x > 0 and max_y - min_y > 0:
        cv2.rectangle(frame, (min_x, min_y), (max_x, max_y), (255, 0, 0), 2)
        i = i + 1
    cv2.putText(frame, str(i), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), 2, cv2.LINE_AA)
    #cv2.drawContours(frame,contours,-1,(0,0,255),2)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()