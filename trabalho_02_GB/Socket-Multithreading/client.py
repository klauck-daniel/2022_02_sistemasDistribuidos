from http import client
import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DICONNECT'
# pega o endereço IP da máquina. Pode chumbar um valor no lugar da função
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Efetiva a conexão com o servidor
client.connect(ADDR)


# função para envio de mensagem
def send(msg):
    message = msg.encode(FORMAT)
    # primeiro, devemos enviar o tamnho da mensagem
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

#manda mensagem pro server
send('Olá!')
#desconecta do server
send(DISCONNECT_MESSAGE)