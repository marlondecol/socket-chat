from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import datetime as dtm
import os

def clearScreen():
	os.system("cls" if os.name == "nt" else "clear")

def bindAddress():
	try:
		port = input("\n  Informe a porta deste socket (a padrão é 33000): ")
		port = 33000 if not port or not port.isdigit() else int(port)

		clearScreen()

		serverSocket.bind(("", port))

		return port
	except OSError:
		print("\n  Esta porta já está sendo usada! Tente usar uma outra.")

		return bindAddress()

def acceptIncomingConnections():
	while True:
		client, address = serverSocket.accept()

		host, port = address
		print("\n\n  +  {}:{} se conectou!".format(host, port), end="")

		addresses[client] = address
		Thread(target=handleClient, args=(client,)).start()

def handleClient(client):
	opt = int(client.recv(1024).decode("utf-8"))
	
	if opt == 1:
		name = client.recv(1024).decode("utf-8")

		client.send(bytes("\nDigite \\quit para sair.\n", "utf-8"))
		broadcast("[" + dtm.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "] {} se juntou à conversa!".format(name))

		clients[client] = name

		while True:
			msg = client.recv(1024).decode("utf-8")

			if msg == "\\quit":
				host, port = client.getpeername()
				
				client.close()

				del clients[client]

				print("\n\n  -  {}:{} deixou o servidor.".format(host, port), end="")
				broadcast("[" + dtm.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "] {} deixou a conversa.".format(name))
				break

			broadcast("[" + dtm.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "] " + name + ": " + msg)

def broadcast(msg):
	for sock in clients:
		sock.send(bytes(msg, "utf-8"))

clearScreen()

clients = {}
addresses = {}

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = bindAddress()

print("\n  Utilizando a porta {}.".format(serverPort))

serverSocket.listen(5)

print("\n  Aguardando a primeira conexão...", end="")

acceptThread = Thread(target=acceptIncomingConnections)

acceptThread.start()
acceptThread.join()

serverSocket.close()