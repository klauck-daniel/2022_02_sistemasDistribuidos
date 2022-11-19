# Aplicativo que publica a mensagem MQTT quando alguma mercadoria ENTRA no estoque

import paho.mqtt.client as mqtt
import sys
import socket
import time

# instancia o paho client
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("stockInComming")#aqui pode inserir o clientName
topic = "test/status"
msg = "Default message."


# cria a conexão com o broker e verifica se a conexão deu certo
if client.connect(mqttBroker) != 0:
    print("Sem conexão com o broker!")
    sys.exit(-1)

while True:
    #ARGUMENTOS(tópico, mensagem de payload, nível de qualidade do serviço)
    client.publish(topic, msg, 0)
    print("Mensagem publicada -> Topico:" + topic + " Mensagem: " + msg)
    time.sleep(1)

#desconecta do broekr
#client.disconnect()
