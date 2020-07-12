#Script that plays piano tiles

from PIL import ImageGrab
import numpy as np
import cv2
import win32api, win32con
import time
import keyboard
time.sleep(3)
startone = [0,513,616,748,851]

def click(x, y):
  win32api.SetCursorPos((x, y))
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
lower_blue = np.array([0, 0, 0,])
upper_blue = np.array([180, 255, 30])
i=0
click(startone[2],481)
#while True:
# print(win32api.GetCursorPos())
#win32api.SetCursorPos((500, 350))
while(True):
    i=i+1
    img = ImageGrab.grab((0,370,1366,380)) #bbox specifies specific region (bbox= x,y,width,height)
    img_np = np.array(img)
    hsv = cv2.cvtColor(img_np, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    ret, thresh = cv2.threshold(mask, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if i < 700:
            click(int(x + (w / 2)), 380)
        elif i>700:
            click(int(x + (w / 2)), 400)
        elif i>900:
            click(int(x + (w / 2)), 420)
        elif i>1000:
            click(int(x + (w / 2)), 440)
        #elif i>1100:
        #    click(int(x + (w / 2)), 470)
        #print (center)
    #cv2.drawContours(img_np, contours, -1, (0, 255, 0), 3)
    #cv2.imshow("test", img_np)
    #cv2.waitKey(25)
