#!/usr/bin/python3

# importando bibliotecas

import socket

# Variaveis
hostnameServidor = "localhost" # endereço do servidor
porta = 1200 # porta de comunicaçãocom o servidor
tamanhoBuffer = 2*(1024) #tamanho em bytes

# Criando Sockets Não Bloqueante UDP em IPv6
chatCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#chatCliente.setblocking(False)
chatCliente.connect((hostnameServidor,porta))


try:
    while True:
        recebeMensagem = chatCliente.recv(tamanhoBuffer)
        print(recebeMensagem)

except KeyboardInterrupt:
    chatCliente.close()