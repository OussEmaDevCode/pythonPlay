from pygame import mixer  # Load the required library
import sounddevice as sd
import numpy as np
import time
#------------------------------------shut up
mixer.init()
mixer.music.load('C:/Users/oussa/PycharmProjects/capture/venv/hi.mp3')
duration = 100  # seconds
i = 0
def print_sound(indata, outdata, frames, tim, status):
    volume_norm = int(np.linalg.norm(indata) * 10)
    print(volume_norm)
    if volume_norm > 10:
      if mixer.music.get_busy()==0:
        mixer.music.play()
    elif mixer.music.get_busy() ==1:
        #time.sleep(0.2)
        mixer.music.stop()



with sd.Stream(callback=print_sound):
    sd.sleep(duration * 1000)
