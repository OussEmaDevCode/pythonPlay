import tkinter as tk
import random
import time
import ctypes
#---------------------------------------------error thing
top = tk.Tk()
class MessageWindow(tk.Toplevel):
    def __init__(self, title,x,y):
        super().__init__()
        def messageshow():
            for x in range(random.randint(10,18)):
                MessageWindow("Fatal Eror",random.randint(00,1066),random.randint(0,668))
        def disable_event():
            pass
        self.details_expanded = False
        self.title(title)
        self.geometry("300x75+{}+{}".format(x,y))
        self.resizable(False, False)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.protocol("WM_DELETE_WINDOW",disable_event )
        tk.Label(self, image="::tk::icons::error").grid(row=0, column=0, pady=(7, 0), padx=(7, 7), sticky="e")
        tk.Label(self, text="Are you sure you want to quit?").grid(row=0, column=1, columnspan=2, pady=(7, 7),sticky="w")
        tk.Button(self, text="Shut down", command = messageshow).grid(row=1, column=2, sticky="e",padx=(7, 7))
        self.iconbitmap(r'C:\social svg\smile.ico')
top.geometry("0x0")
top.overrideredirect(1)
user32 = ctypes.windll.user32
MessageWindow("Fatal Error",int(user32.GetSystemMetrics(0)/2),int(user32.GetSystemMetrics(1)/2))
top.mainloop()
