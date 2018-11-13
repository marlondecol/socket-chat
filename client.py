from socket import socket, gaierror, AF_INET, SOCK_STREAM
from threading import Thread
import os

def clearScreen():
	os.system("cls" if os.name == "nt" else "clear")

# Permite a leitura de um arquivo.
#
# É informado o caminho completo,
# o código faz as verificações necessárias
# e retorna o objeto do arquivo para manipulá-lo.
def readFile(file):
	try:
		# Verifica o caminho do arquivo.
		if file[0] != "/":
			file = os.getcwd() + "/" + file

		# Recebe o caminho absoluto até o arquivo.
		file = os.path.abspath(file)

		# Se o arquivo existe, o mesmo é obtido
		# em modo binário (letra "b" do segundo parâmetro)
		return open(file, "rb")
	except OSError:
		# Se o arquivo não existe, exibe um feedback.
		print("\n  Arquivo inexistente!\n")

	exit()

# Cria um arquivo se acordo com os parâmetros informados.
#
# O sufixo é incrementado toda vez
# que há um arquivo com o mesmo nome.
def createFile(file):
	try:
		# Caso o arquivo não existe, cria-o,
		# também em modo binário, e retorna-o.
		return open(file, "xb")
	except FileExistsError:
		# Se o arquivo já existe, exclui o mesmo
		# para que possa ser substituído.
		os.remove(file)

		# E tenta criar o arquivo novamente.
		return createFile(file)
	except Exception:
		# Exibe um feedback caso ocorra um erro inesperado.
		print("\n  Um erro inesperado ocorreu!\n")

	exit()

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
		print("\n  Endereço dessconhecido! Tente novamente.")
	except ValueError:
		clearScreen()

		print("\n  Endereço ou porta inválido!")

	return connectSocket()

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

def receiveFile():

def sendFile():
	filename = input("Nome do arquivo: ")
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

		clientSocket.send(bytes(msg, "utf-8"))

		if msg == "\\quit":
			break

		if msg == "\\file":
			sendFile()
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
	elif opt == 2:
		host = input("\n  Digite o endereço do host: ")
		port = input("  Digite a porta do host: ")

print()