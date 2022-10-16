#FONTE https://www.youtube.com/watch?v=QyJBrS1c1s8
import threading
import socket

clients = []

redLed = 0
greenLed = 0

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
            if(msg == 'tmpRead'):
                tmpReader()
            elif(msg =='powerLed'):
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


#desenvolver método para separar deserializar os valores das mensagens que chegam
#colocar alguns prints no servidor para ir logando as mensagens


def tmpReader():
    dhtTemperature = 21; #colocar funcção para gerar valores aleatórios dentro de um range
    return dhtTemperature()

def powerLed(msg):
    if(msg == "powerGreenLed"):
        if(redLed == 1):
            redLed = 0
        greenLed = 1
    elif(msg == "powerRedLed"):
        if(greenLed == 1):
            greenLed = 0
        redLed = 1


main()
