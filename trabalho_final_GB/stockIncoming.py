# Aplicativo que publica a mensagem MQTT quando alguma mercadoria ENTRA no estoque

import paho.mqtt.client as paho
import sys
import socket
import time

# instancia o paho client
client = paho.Client()

# cria a conexão com o broker e verifica se a conexão deu certo
if client.connect("localhost", 1883, 60) != 0:
    print("Not conected do MQTT broker!")
    sys.exit(-1)

#ARGUMENTOS(tópico, mensagem de payload, nível de qualidade do serviço)
client.publish("test/status", "Helloworld from paho-mqtt!", 0)

#desconecta do broekr
client.disconnect()
