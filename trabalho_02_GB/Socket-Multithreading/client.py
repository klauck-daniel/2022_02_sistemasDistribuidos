# Protocolo das mensagens
# TMP_READ - Ler temperatura
# TMP_XXXX - Temperatura Lida
# LED_GREEN - Ligar led verde
# LED_RED - Ligar led vermelho

from http import client
import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
TMP_READ = 'TMP_READ'
LED_GREEN = 'LED_GREEN'
LED_RED = 'LED_RED'
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
    recvmsg = client.recv(2048).decode(FORMAT)
    print(recvmsg) 
    if msg == TMP_READ:
        recsvmsgfloat = float(recvmsg[4:9])
        print(recsvmsgfloat)
        ledToTurnOn = LED_GREEN
        if not recsvmsgfloat<30:
            ledToTurnOn = LED_RED
        send(ledToTurnOn)
        print(f"{ledToTurnOn} será ligado")
        


    



# manda mensagem pro server
send(TMP_READ)
input()
# desconecta do server
send(DISCONNECT_MESSAGE)
