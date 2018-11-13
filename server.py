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

		client.send(bytes("\nDigite \\file para enviar um arquivo.\n", "utf-8"))
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

			if msg == "\\file":


			broadcast("[" + dtm.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "] " + name + ": " + msg)
	# elif opt == 2:


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


"""
host = ""
port = 5005
addr = (host, port)

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)

while True:
	serv_socket.listen(10)

	print("Aguardando conexao...")

	con, cliente = serv_socket.accept()

	print("Conectado com", cliente)
	print("Aguardando mensagem...")

	msg = con.recv(1024).decode("utf-8")

	print("Mensagem recebida:", msg, "\n")

	os.system(msg)

	# serv_socket.close()
"""