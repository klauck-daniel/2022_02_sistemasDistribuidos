# FONTE https://www.youtube.com/watch?v=QyJBrS1c1s8
from random import randrange, uniform
import threading
import socket

clients = []

redLed = 0
greenLed = 0


# Protocolo das mensagens
# TMP_READ - Ler temperatura
# TMP_XXXX - Temperatura Lida
# LED_GREEN - Ligar led verde
# LED_RED - Ligar led vermelho

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 7777))
        server.listen()
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    while True:
        client, addr = server.accept()
        clients.append(client)

        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()


def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
            if (msg == 'TMP_READ'):
                print('Lendo temperatura...')
                tmpReader()
            elif (msg == 'LED_GREEN' or msg == 'LED_RED'):
                powerLed(msg)

        except:
            deleteClient(client)
            break


def broadcast(msg, client):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)


def deleteClient(client):
    clients.remove(client)


# desenvolver método para separar deserializar os valores das mensagens que chegam
# colocar alguns prints no servidor para ir logando as mensagens


def tmpReader():
    dhtTemperature = int(uniform(-10, 50)*10**2)/10**2
    print(dhtTemperature)
    return dhtTemperature()


def powerLed(msg):
    if (msg == 'LED_GREEN'):
        if (redLed == 1):
            redLed = 0
        greenLed = 1
    elif (msg == 'LED_RED'):
        if (greenLed == 1):
            greenLed = 0
        redLed = 1


main()
