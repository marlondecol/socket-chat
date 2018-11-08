from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from os import system

def receive():
    while True:
        msg = clientSocket.recv(1024).decode()

        if msg == "\\quit":
            clientSocket.close()
            break

        if not msg:
            break

        print(msg)

def send():
    while True:
        msg = input()

        clientSocket.send(bytes(msg, "utf-8"))

        if msg == "\\quit":
            break

clientHost = "localhost"
clientPort = 33000

if not clientPort:
    clientPort = 33000
else:
    clientPort = int(clientPort)

address = (clientHost, clientPort)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(address)

receiveThread = Thread(target=receive)
sendThread = Thread(target=send)

receiveThread.start()
sendThread.start()

receiveThread.join()
sendThread.join()