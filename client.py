from threading import Thread
import socket as skt
import os

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

	opt = input("\n  Sua opção: ")

	clearScreen()

	if not opt or not opt.isdigit() or int(opt) not in menuOptions.keys():
		print("\n  Opção inválida! Tente novamente.")
		return showMenu()

	return int(opt)

def send(msg):
	clientSocket.send(bytes(msg, "utf-8"))

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

		send(msg)

		if msg == "\\quit":
			break

while True:
	clearScreen()

	opt = showMenu()

	if not opt:
		break

	if opt == 1:
		host = input("\n  Digite o endereço do host: ")

		if not host:
			break

		port = input("  Digite a porta do host: ")

		if not port or not port.isdigit():
			break

		port = int(port)

		address = (host, port)

		clientSocket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

		clientSocket.connect(address)

		send(str(opt))

		clearScreen()

		print("\n  Seja bem-vindo!\n")
		
		send(input("  Diga para seus amigos quem é você: "))

		clearScreen()

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

"""
import socket as skt

ip = input("Digite o IP para conexão: ")
port = 5005
addr = (ip, port)

clientSocket = sktsocket(sktAF_INET, sktSOCK_STREAM)

clientSocket.connect(addr)
clientSocket.send(bytes(input("Digite uma mensagem para enviar ao servidor: "), "utf-8"))

print("Mensagem enviada!")

clientSocket.close()
"""