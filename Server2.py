#Two way chat
import socket
import sys
import time

s=socket.socket()
host=socket.gethostname()
print("Server will start on host: ",host)
port=8080
s.bind((host,port))
print("Server has done binding")
print("Server is waiting for incoming connection")
s.listen(1)
conn,addr=s.accept()
print(addr," has connected to the server and is now online")
while True:
	message=input(">>")
	message=message.encode()
	conn.send(message)
	print("Message has been sent")
	print("")
	incoming_msg=conn.recv(1024)
	incoming_msg=incoming_msg.decode()
	print("Client: ",incoming_msg)
	print("")