from socket import socket, gaierror, AF_INET, SOCK_STREAM
from threading import Thread
import os, time

def clearScreen():
	os.system("cls" if os.name == "nt" else "clear")

def connectSocket():
	try:
		host = input("\n  Digite o endereço do host: ")

		if not host:
			raise ValueError

		port = int(input("  Digite a porta do host: "))

		clearScreen()

		clientSocket.connect((host, port))

		return
	except ConnectionRefusedError:
		print("\n  A conexão com este endereço foi recusada! Tente novamente.")
	except gaierror:
		print("\n  Endereço desconhecido! Tente novamente.")
	except ValueError:
		clearScreen()

		print("\n  Endereço ou porta inválido!")

	return connectSocket()

def showMenu():
	menuOptions = {
		1: "Conversar",
		0: "Sair"
	}

	print("\n  O que deseja fazer?\n")
	
	for n, d in menuOptions.items():
		print("  [{}] {}".format(n, d))

	opt = input("\n  Sua opção: ")

	clearScreen()

	if not opt or not opt.isdigit() or int(opt) not in menuOptions.keys():
		print("\n  Opção inválida! Tente novamente.")
		return showMenu()

	return int(opt)

def receiveMessage():
	while True:
		msg = clientSocket.recv(1024).decode("utf-8")

		if msg == "\\quit":
			clientSocket.close()
			break
		
		if not msg:
			break

		print(msg)

def sendMessage():
	while True:
		msg = input()

		clientSocket.send(bytes(msg, "utf-8"))

		if msg == "\\quit":
			break

while True:
	clearScreen()

	opt = showMenu()

	if not opt:
		break

	if opt == 1:
		clientSocket = socket(AF_INET, SOCK_STREAM)

		connectSocket()

		clientSocket.send(bytes(str(opt), "utf-8"))

		print("\n  Seja bem-vindo!\n")
		
		clientSocket.send(bytes(input("  Diga para seus amigos quem é você: "), "utf-8"))

		clearScreen()

		receiveThread = Thread(target=receiveMessage)
		sendThread = Thread(target=sendMessage)

		receiveThread.start()
		sendThread.start()

		receiveThread.join()
		sendThread.join()

print()