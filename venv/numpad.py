import socket
import time
from pynput.keyboard import Key, Controller
from multiprocessing import Process
import sys
#------------------------------------------detects numpad
keyboard = Controller()
#Defines Server Values
listensocket = socket.socket()
Port = 8000
maxConnections = 9999
IP = socket.gethostbyname(socket.gethostname()) #Gets Hostname Of Current Macheine
stop = True
listensocket.bind(("0.0.0.0",Port))
#Opens Server
listensocket.listen(maxConnections)
print("Server started at " + IP + " on port " + str(Port))
while True:
 #Accepts Incomming Connection
 (clientsocket, address) = listensocket.accept()
 print("New connection made!")

#Main1
 while True:
     message = clientsocket.recv(1024).decode() #Receives Message
     print(message)
     #Turns On LED
     if not message == "":
        if message == "enter" :
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        else:
            keyboard.press(message)

    # closes Server If Message Is Nothing (Client Terminated)
     else:
         clientsocket.close()
         break