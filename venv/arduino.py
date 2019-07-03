import bluetooth
hostMACAddress = '98:D3:51:F5:A8:84' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 1
backlog = 1
size = 9600
sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )  
sock.connect((hostMACAddress, port))  
client, clientInfo = sock.accept()
while 1:
      data = client.recv(size).decode()
      if data:
          print(data)  # Echo back to client


