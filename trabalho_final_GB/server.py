# Aplicação do server.
# Recebe as mensagens MQTT e faz o incremento ou decremento da contagem do estoque
# Gera relatório com a quantidade de itens no estoque

# Aplicativo que Recebe a mensagem MQTT quando alguma mercadoria ENTRA ou SAI do estoque

import paho.mqtt.client as mqtt
import sys
#import socket
import time

def on_message(client, userdata, message):
    print("Mensagem recebida: ", str(message.payload.decode("utf-8")))


# instancia o paho client
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("server")  # aqui pode inserir o clientName
topic = "test/status"
msg = "Default message."

# precisamos subescrever um client que está em loop, então precisamos de um loop
client.loop_start()
#Subescrevendo o tópico
client.subscribe(topic)
#callback das mensagens
client.on_message = on_message
time.sleep(5)
client.loop_stop()

# cria a conexão com o broker e verifica se a conexão deu certo
'''if client.connect(mqttBroker) != 0:
    print("Sem conexão com o broker!")
    sys.exit(-1)

while True:
    # ARGUMENTOS(tópico, mensagem de payload, nível de qualidade do serviço)
    client.publish(topic, msg, 0)
    print("Mensagem publicada -> Topico:" + topic + " Mensagem: " + msg)
    time.sleep(1)'''
