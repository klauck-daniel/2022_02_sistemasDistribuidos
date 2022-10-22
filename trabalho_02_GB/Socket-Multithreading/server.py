from http import server
import socket
import threading

HEADER = 64
PORT = 5050
# pega o endereço IP da máquina. Pode chumbar um valor no lugar da função
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DICONNECT'


# Ligar um socket ao endereço IP e Porta
# Mudar parametro  socket.SOCK_STREAM caso não queira fazer stream dos dados
#server = socket.socket(socket.FAMILIA, socket.TIPOM)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# vincular o socket a um endereço
server.bind(ADDR)

# Configurar o socket para ouvir e imprimir algumas coisas e esperar novas conexões

'''Esse método deve ser colocado em threads para que
a linha que aguarda mensagens do cliente não bloquei
novas conexões'''


def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected')

    connected = True
    while connected:

        # informa o tamanho da mensagem que irá chegar
        msg_length = conn.recv(HEADER).decode(FORMAT)
        # caso a mensagem tenha algum conteúdo
        if msg_length:
            # converte o tamanho da mensagem em um integer
            msg_length = int(msg_length)
            # recebe a mensagem, ja com o tamanho definido
            msg = conn.recv(msg_length).decode(FORMAT)
            # desconexão do usuário
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f'[{addr}] {msg}')
            #para mandar mensagem de volta para o client
            conn.send('Msg received'.encode(FORMAT))

    conn.close()


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
        # exibe quantidade de conexoes a partir de threads ativas. Uma thread é usada para o prório serve, por isso o "-1"
        print(f'[ACTIVE CONNECTIONS] {threading.active_count()-1}')


print('[STARTING] server is starting...')
start()
