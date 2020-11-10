#!/usr/bin/python3

# importando bibliotecas

import socket
from _thread import *
import sys
import select

# Variaveis
#hostname = socket.gethostname() # endereço público
hostname = "localhost" # endereço local
porta = 12001 # porta de comunicação
tamanhoBuffer = 2*(1024) #tamanho em bytes

# Criando Sockets Bloqueante UDP em IPv6
chatServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
chatServidor.setblocking(True)

chatServidor.bind((hostname, porta)) # Ligação Publica
chatServidor.listen(30) # Maximo de Conexoes simultaneas

mensagem = "testando 123 ..."

def conversa(client_socket, addr):    #Function to manage clients
    client_socket.sendall(mensagem.encode("utf-8"))


try:
    while True:
        clienteSocket, enderecoCliente = chatServidor.accept()
        start_new_thread(conversa,(clienteSocket,enderecoCliente))

        #msg = input("digite: ")
        #mensagem = msg


except KeyboardInterrupt:
    chatServidor.close()

