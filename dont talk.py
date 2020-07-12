# Script that plays a BLAH BLAH BLAH sound whenever somebody talks

from pygame import mixer  # Load the required library
import sounddevice as sd
import numpy as np
import time

mixer.init()
mixer.music.load('./hi.mp3')
duration = 100 # seconds3

threshold = int(input("threshold: "))
def print_sound(indata, outdata, frames, tim, status):
    volume_norm = int(np.linalg.norm(indata) * 10)
    print(volume_norm)
    if volume_norm > threshold and not mixer.get_busy():
        mixer.music.play()
        time.sleep(2);




with sd.Stream(callback=print_sound):
    sd.sleep(duration * 1000)
