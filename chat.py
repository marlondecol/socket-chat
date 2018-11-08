from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import datetime, os

def clearScreen():
	os.system("cls" if os.name == "nt" else "clear")

def showMenu():
	menuOptions = {
		1: "Enviar mensagens e arquivos",
		2: "Acessar terminal remoto",
		0: "Sair"
	}

	print("\n  O que deseja fazer?\n")
	
	for n, d in menuOptions.items():
		print("  [{}] {}".format(n, d))

	opt = int(input("\n  Sua opção: "))

	clearScreen()

	if opt not in menuOptions.keys():
		print("\n  Opção inválida! Tente novamente.")
		return showMenu()

	return opt

def send(msg):
	socket.send(bytes(msg, "utf-8"))

def receiveMessage():
	clearScreen()
	
	while True:
		messages = socket.recv(1024).decode()

		if not messages:
			break

		lastClient = ""

		for client, time, name, text in messages:
			message = "[" + time.strftime("%d/%m/%Y %H:%M:%S") + "] " + name + ": "
			
			if client != lastClient:
				lastClient = client
				message = "\n" + message

			print(message)

		print("\n  {:-^20}".format())

def sendMessage():
	while True:
		msg = input("\n  Digite sua mensagem: ")

		if msg == "\\quit":
			socket.close()
			break

		send(msg)

while True:
	clearScreen()

	opt = showMenu()

	print(not opt)
	break

	if not opt:
		break

	if opt == 1:
		host = input("\n  Digite o endereço do host: ")
		port = input("  Digite a porta do host: ")

		port = 33000 if not port else int(port)

		address = (host, port)

		socket = socket(AF_INET, SOCK_STREAM)
		socket.connect(address)

		send(opt)

		clearScreen()

		print("\n  Seja bem-vindo!\n")
		
		send(input("  Diga para seus amigos quem é você: "))

		receiveThread = Thread(target=receiveMessage)
		sendThread = Thread(target=sendMessage)

		receiveThread.start()
		sendThread.start()

		receiveThread.join()
		sendThread.join()
	elif opt == 2:
		host = input("\n  Digite o endereço do host: ")
		port = input("  Digite a porta do host: ")

print()