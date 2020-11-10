#!/usr/bin/python3

# importando bibliotecas

import socket
from _thread import *
import sys
import select

# Variaveis
#hostname = socket.gethostname() # endereço público
hostname = "localhost" # endereço local
porta = 1345 # porta de comunicação

chatServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
chatServidor.bind((hostname, porta))
chatServidor.listen(2)

def fatorial (numeroInteiro):
    tamanho = numeroInteiro + 1
    calculo = 1
    for i in range(1,tamanho):
        calculo = calculo * i
    return calculo

while True:

    clienteSocket, enderecoCliente = chatServidor.accept()

    mensagem = chatServidor.recv(1024)

    mensagem = mensagem.decode("ascii")
    #valor = int(mensagem)

    #fat = fatorial(valor)

    print(mensagem)

    #mensagem = str(fat).encode("utf-8")

    #clienteSocket.send(mensagem)



