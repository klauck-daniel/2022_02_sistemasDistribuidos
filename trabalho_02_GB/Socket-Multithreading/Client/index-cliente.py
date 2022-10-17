import threading
import socket

tmpResponse = 0

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 7777))
    except:
        return print('\nNão foi possívvel se conectar ao servidor!\n')

    username = input('Usuário> ')
    print('\nConectado')


# Criar duas threads para rodar as funções receiveMessages e sendMessage ao mesmo tempo
    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client, username])

    thread1.start()
    thread2.start()


def receiveMessages(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(msg+'\n')
        except:
            print('\nNão conectado ao servidor!\n')
            print('Pressione <Enter> para continuar...')
            client.close()
            break


def sendMessages(client, username):
    while True:
        try:
            msg = input('\n')
            client.send(f'<{username}> {msg}'.encode('utf-8'))
        except:
            return


def tmpRequest():
    # caso o temporizador tenha valor maior que 60s, solicitar leitura de temperatura
    pass


def tmpProcess():
    if(tmpResponse < 30):
        # request ao servidor para powerGreenLed
        print(f'Led VERDE será LIGADO. Temperadura de {tmpResponse} ºC.')
        
    else:
        # request ao servidor para powerRedLed
        print(f'Led VERMELHO será LIGADO. Temperadura de {tmpResponse} ºC.')
        pass

main()
