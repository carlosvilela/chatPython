#!/usr/bin/python3

# importando bibliotecas
import socket

# Variaveis
hostname = "localhost"                                                          # endereço local
porta = 1404                                                                    # porta de comunicação
tamanhoBuffer = 4*(1024)                                                        # Tamanho do Buffer

# Criando Sockets TCP em IPv6
chatServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                # Cria Socket TCP
chatServidor.bind((hostname, porta))                                            # hostname e porta de acesso
chatServidor.listen(30)                                                         # numero de Conexões permitidas

# Função para calcular o fatorial de um numero
def fatorial (numeroInteiro):
    tamanho = numeroInteiro + 1
    calculo = 1
    for i in range(1,tamanho):
        calculo = calculo * i
    return calculo

# Loop infinito, aguardando requisições
try:                                                                        # tratamento de erros
    while True:
        clienteSocket, enderecoCliente = chatServidor.accept()              # Espera por conexão do cliente
        mensagem = clienteSocket.recv(tamanhoBuffer)                        # recebe a mensagem do Cliente
        mensagem = mensagem.decode("ascii")                                 # converte os bytes na tabela ascii
        valor = int(mensagem)                                               # converte a string em numero inteiro
        fat = fatorial(valor)                                               # realiza os calculos
        mensagem = str(fat).encode("utf-8")                                 # converte o numero inteiro em string
        clienteSocket.send(mensagem)                                        # retorna a mensagem processada ao cliente

except KeyboardInterrupt:                                                   # caso haja erro irá retornar uma ação
    chatCliente.close()                                                     # finaliza conexão, finaliza o servidor

