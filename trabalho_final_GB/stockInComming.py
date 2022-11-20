# Aplicativo que publica a mensagem MQTT quando alguma mercadoria ENTRA no estoque

import paho.mqtt.client as mqtt
import sys
import socket
import time
import keyboard

# instancia o paho client
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("stockInComming")  # aqui pode inserir o clientName
topic = "stock/in"
msg = "Inventory product entry detected!"


# cria a conexão com o broker e verifica se a conexão deu certo
if client.connect(mqttBroker) != 0:
    print("No connection to the broker!")
    sys.exit(-1)

while True:
    # ARGUMENTOS(tópico, mensagem de payload, nível de qualidade do serviço)
    if keyboard.read_key() == "u":
        client.publish(topic, msg, 0)
        print("Message published -> Topic: " + topic + " Message: " + msg)
        client.publish(topic, "1", 0)
        print("Item packaging-> Unity.")
        time.sleep(1)
    if keyboard.read_key() == "p":
        client.publish(topic, msg, 0)
        print("Message published -> Topic: " + topic + " Message: " + msg)
        client.publish(topic, "2", 0)
        print("Item packaging-> Pack.")
        time.sleep(1)    
    if keyboard.read_key() == "b":
        client.publish(topic, msg, 0)
        print("Message published -> Topic: " + topic + " Message: " + msg)
        client.publish(topic, "3", 0)
        print("Item packaging-> Box")
        time.sleep(1)    

# desconecta do broekr
# client.disconnect()
