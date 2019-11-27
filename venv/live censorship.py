from pynput.keyboard import Key, Listener , Controller
import ctypes
import keyboard
import time
#------------------------prevent you from cursing
class txt :
    bad = ["fuck","bich","bitch", "shit","nigga","ass","nigger","terrorist","banana skin","lemon","fuxk","bicj","dick","gay","dic"]
    t = ""
def on_press(key):
    if key == Key.space:
      txt.t += ""
    elif key == Key.backspace:
     txt.t = txt.t[:-1]
    elif key ==Key.caps_lock or key== Key.enter:
        pass
    else:
      txt.t += str(key).replace("'","")
    for badword in txt.bad:
        if txt.t.lower().find(badword) != -1 :
            keyboard = Controller()
            for x in range(len(badword)):
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
            break
    print(txt.t)
with Listener(on_press=on_press) as listener:
    listener.join()
