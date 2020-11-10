#!/usr/bin/python3

# importando bibliotecas

import socket
import sys
import select

# Variaveis
#hostname = socket.gethostname() # endereço público
hostname = "localhost" # endereço local
porta = 1345 # porta de comunicação
tamanhoBuffer = 2*(1024) #tamanho em bytes

# Criando Sockets Bloqueante UDP em IPv6
chatCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # UDP

chatCliente.connect((hostname, porta))

while True:
    enviar = input("Digite o primeiro numero: ")
    chatCliente.send(enviar.encode())

    #resultado = chatCliente.recv(1048)

    #print("O Fatorial de",enviar," e = ",resultado)

