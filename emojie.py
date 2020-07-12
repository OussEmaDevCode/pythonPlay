#Script that replaces ASCII textual emojies with actual emojies 

from pynput.keyboard import Key, Listener , Controller
import ctypes
import keyboard
import time
import pyperclip
import sys
import ctypes  # An included library with Python install.

ctypes.windll.user32.MessageBoxW(0, "EmojiBot started looking fo some emojies to swap, press ctrl+alt+F2 to stop", "Start up", 64)

class txt :
    emojies = {":)":"😃"  ,  ":\"":"😘"  ,  ":q":"😋"  ,  ":(":"😟" , ":o":"😱"    ,  ":x":"😵",
               ":z":"😴"  ,  ":p":"💩"  ,  ":l":"😐"  , ";)":"😉" ,  ":$":"🤑"  ,  ":v":"🤣"}
    t = ""
    ext = str(Key.ctrl) + str(Key.alt)+str(Key.f2)
    stop = True

def on_press(key):
    if txt.stop :
      if key == Key.space:
        txt.t += ""
      elif key == Key.backspace:
        txt.t = txt.t[:-1]
      elif  key== Key.enter:
        pass
      else:
        txt.t += str(key).replace("'","")
      for emoji in txt.emojies:
        if txt.t.lower().find(emoji) != -1 :
            keyboard = Controller()
            for x in range(len(emoji)-1):
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
            pyperclip.copy(txt.emojies.get(emoji))
            keyboard.press(Key.ctrl)
            keyboard.press("v")
            keyboard.release("v")
            keyboard.release(Key.ctrl)
            txt.t = ""
            break
    #if :
    if all(elem in list(txt.t)  for elem in list(txt.ext)):
      txt.stop = False
      #exit()
      #sys.exit()

with Listener(on_press=on_press) as listener:
    listener.join()
