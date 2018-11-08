from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import datetime as dtm

def acceptIncomingConnections():
    while True:
        client, address = serverSocket.accept()
        host, port = address

        print("{}:{} se conectou!".format(host, port))

        client.send(bytes("Olá! Digite seu nome e pressione [ENTER]: ", "utf-8"))
        addresses[client] = address
        Thread(target=handleClient, args=(client,)).start()

def handleClient(client):
    name = client.recv(1024).decode()
    
    client.send(bytes("Bem-vindo {}! Se quiser sair, digite \\quit quando quiser.".format(name), "utf-8"))
    broadcast(bytes("{} se juntou à conversa!".format(name), "utf-8"))
    
    clients[client] = name

    while True:
        msg = client.recv(1024)
        
        if msg != bytes("\\quit", "utf-8"):
            broadcast(msg, "[" + dtm.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "] " + name + ": ")
        else:
            client.send(bytes("\\quit", "utf-8"))
            client.close()

            del clients[client]
            
            broadcast(bytes("{} deixou a conversa.".format(name), "utf-8"))
            
            break

def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf-8") + msg)

clients = {}
addresses = {}

serverHost = ""
serverPort = input("Informe a porta que deseja liberar para o chat: ")

serverPort = 33000 if not serverPort else int(serverPort)

address = (serverHost, serverPort)

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(address)

print("Utilizando a porta {}".format(serverPort))

if __name__ == "__main__":
    serverSocket.listen(5)

    print("Esperando por conexões...")
    
    acceptThread = Thread(target=acceptIncomingConnections)
    
    acceptThread.start()
    acceptThread.join()
    
    serverSocket.close()