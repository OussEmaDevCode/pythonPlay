from PIL import ImageGrab
import numpy as np
import cv2
import time
#--------------------------------detects objects with colrs

cap = cv2.VideoCapture(0)
lower_blue = np.array([ -3  ,55, 108])
upper_blue = np.array([17  ,75 ,188])
while(True):
    #img = ImageGrab.grab((500,560,660,600)) #bbox specifies specific region (bbox= x,y,width,height)
    #img_np = np.array(img)
    ret ,img_rgb = cap.read()
    hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    ret, thresh = cv2.threshold(mask, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    try:
        hierarchy = hierarchy[0]
    except:
        hierarchy = []
    i=0
    for contour, hier in zip(contours, hierarchy):
        (x, y, w, h) = cv2.boundingRect(contour)
        if w > 80 and h > 100:
            cv2.rectangle(img_rgb, (x, y), (x + w, y + h), (255, 0, 0), 2)
            i = i + 1
    print(i)
    #cv2.drawContours(img_rgb, contours, -1, (255, 0, 0), 3)
    cv2.imshow("test",img_rgb)
    cv2.waitKey(25)