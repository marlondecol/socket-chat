import socket

ip = input("Digite o IP para conexão: ")
port = 5005
addr = (ip, port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(addr)
client_socket.send(bytes(input("Digite uma mensagem para enviar ao servidor: "), "utf-8"))

print("Mensagem enviada!")

client_socket.close()