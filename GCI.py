#Script that takes screenshots, reads text in them and notifies me about something

from PIL import ImageGrab
import numpy as np
import cv2
import time
import io
import json
import requests
from gtts import gTTS
import os

past = '';
repeat = False;

x = int(input("What's your x ?"))
y = int(input("What's your y ?"))
width = x + int(input("What's your width ?"))
height = y + int(input("what's your height ?"))

while(True):
    img = ImageGrab.grab((x,y,width,height)) #bbox specifies specific region (bbox= x,y,width,height)
    img = np.array(img)
    _, compressedimage = cv2.imencode(".jpg", img, [1, 90])
    file_bytes = io.BytesIO(compressedimage)
    result = requests.post("https://api.ocr.space/parse/image",
                           files={"screenshot.jpg": file_bytes},
                           data={"apikey": "a4ecb5ab5b88957",
                                 "language": "eng"})
    text_detected = json.loads(result.content.decode()).get("ParsedResults")[0].get("ParsedText")
    if past != text_detected and text_detected:
        if repeat:
            past = text_detected;
            fileName = "message"+".mp3";
            gTTS(text=past, lang="en", slow=False).save(fileName)
            os.system(fileName)
        else:
            past = text_detected
    print(text_detected)
    repeat = True;
    cv2.imshow("preview", img)
    cv2.waitKey(25)
