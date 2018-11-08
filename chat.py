import socket as sk
import os

def clear():
	os.system("cls" if os.name == "nt" else "clear")

def send(sk, msg):
	client_socket.send(bytes(input("Digite uma mensagem para enviar ao servidor: "), "utf-8"))

serverHost = ""
serverPort = 5005

serverAddress = (serverHost, serverPort)

serverSocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

serverSocket.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR, 1)
serverSocket.bind(addr)

while True:
	clear()

	print("\n  O que deseja fazer?\n")

	print("  [1] Enviar mensagens")
	print("  [2] Acessar terminal remoto")
	print("  [0] Sair\n")

	opt = int(input("  Sua opção: "))

	if not opt: break

	clear()

	if opt == 1:
		chat = list()

		while True:
			print("\n  Digite \\quit para sair")
			print("\n  ----------\n")

			for time, name, msg in chat:
				print("  [" + time + "] " + name + ": " + msg + "\n")

			serverSocket.listen(10)

			
		# ip = input("\n  IP do destinatário: ")
	# elif opt == 2:

	"""

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
		"""
print()