# Protocolo das mensagens
# TMP_READ - Ler temperatura
# TMP_XXXX - Temperatura Lida
# LED_GREEN - Ligar led verde
# LED_RED - Ligar led vermelho

from http import server
from random import randrange, uniform
import socket
import threading

HEADER = 64
PORT = 5050
# pega o endereço IP da máquina. Pode chumbar um valor no lugar da função
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
TMP_READ = 'TMP_READ'
LED_GREEN = 'LED_GREEN'
LED_RED = 'LED_RED'


# Ligar um socket ao endereço IP e Porta
# Mudar parametro  socket.SOCK_STREAM caso não queira fazer stream dos dados
# Configurar o socket para ouvir e imprimir algumas coisas e esperar novas conexões
#server = socket.socket(socket.FAMILIA, socket.TIPOM)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# vincular o socket a um endereço
server.bind(ADDR)

'''Esse método deve ser colocado em threads para que
a linha que aguarda mensagens do cliente não bloquei
novas conexões'''


def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected')

    connected = True
    while connected:

        STATUS_GREEN = 0
        STATUS_RED = 0
        # informa o tamanho da mensagem que irá chegar
        msg_length = conn.recv(HEADER).decode(FORMAT)
        # caso a mensagem tenha algum conteúdo
        if msg_length:
            # converte o tamanho da mensagem em um integer
            msg_length = int(msg_length)
            # recebe a mensagem, ja com o tamanho definido
            msg = conn.recv(msg_length).decode(FORMAT)
            
            # recebendo solicitação de temperatura e retorna ao client
            if msg == TMP_READ:
                conn.send(
                    f'TMP_{tmp_measure():,.2f} \nMsg received by server'.encode(FORMAT))

            # recebe solicitação para ligar ou desligar os leds
            elif msg == LED_GREEN or msg == LED_RED:
                # chama função handle_led e guarda na tupla LED_STATUS
                LED_STATUS = handle_led(msg, STATUS_GREEN, STATUS_RED)

                # LED_STATUS[0] corresponde ao led VERDE
                if LED_STATUS[0] == 1:
                    conn.send(
                        f'[LOG LED STATUS] GREEN = {LED_STATUS[0]} - [LOG LED STATUS] RED = {LED_STATUS[1]} \nMsg received by server'.encode(FORMAT))

                # LED_STATUS[1] corresponde ao led VERMELHO
                elif LED_STATUS[1] == 1:
                    conn.send(
                        f'[LOG LED STATUS] RED = {LED_STATUS[1]} - [LOG LED STATUS] GREEN = {LED_STATUS[0]} \nMsg received by server'.encode(FORMAT))

            # desconexão do usuário
            elif msg == DISCONNECT_MESSAGE:
                connected = False

            print(f'[{addr}] {msg}')

    conn.close()

# Define o status dos LEDs


def handle_led(msg, STATUS_GREEN, STATUS_RED):

    if msg == LED_GREEN:
        STATUS_GREEN = 1
        STATUS_RED = 0
        print(f'[STATUS_GREEN] {STATUS_GREEN} e [STATUS_RED] {STATUS_RED}')
    elif msg == LED_RED:
        STATUS_GREEN = 0
        STATUS_RED = 1
        print(f'[STATUS_GREEN] {STATUS_GREEN} e [STATUS_RED] {STATUS_RED}')
    else:
        STATUS_GREEN = 0
        STATUS_RED = 0
        print(f'[STATUS_GREEN] {STATUS_GREEN} e [STATUS_RED] {STATUS_RED}')

    return (STATUS_GREEN, STATUS_RED)


# gera valor aleatório para retornar como temperatura
def tmp_measure():
    return (uniform(-10, 50)*10**2)/10**2


def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')
    while True:
        '''conn e addr armazenam IP e PORTA da conexão para
        poder mandar mensagens de volta'''
        conn, addr = server.accept()  # Esta linha aguarda uma nova conexão ao servidor
        thread = threading.Thread(target=handle_client, args=(
            conn, addr))  # passa a nova conexão ao handle
        thread.start()
        # exibe quantidade de conexoes a partir de threads ativas.
        # Uma thread é usada para o prório serve, por isso o "-1"
        print(f'[ACTIVE CONNECTIONS] {threading.active_count()-1}')


print('[STARTING] server is starting...')
start()
