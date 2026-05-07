import socket

s = socket.socket()

s.bind(("localhost", 1234))

s.listen(1)

print("Waiting for connection...")

c, addr = s.accept()

print("Connected")

msg = c.recv(1024).decode()

print("Client:", msg)

c.send("Hello Client".encode())

c.close() 

type in terminal1
python3 server.py

import socket

s = socket.socket()

s.connect(("localhost", 1234))

s.send("Hello Server".encode())

msg = s.recv(1024).decode()

print("Server:", msg)

s.close()

type in terminal 2

python3 client.py