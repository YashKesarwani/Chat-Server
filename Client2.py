import socket
import sys
import time

s=socket.socket()
host=input("Plese enter the hostname of server: ")
port=8080
s.connect((host,port))
print("Connected to chat server")
while True:
	incoming_msg=s.recv(1024)
	incoming_msg=incoming_msg.decode()
	print("Server: ",incoming_msg)
	print("")
	message=input(">>")
	message=message.encode()
	s.send(message)
	print("Message has been sent")
	print("")