# Aplicação do server.
# Recebe as mensagens MQTT e faz o incremento ou decremento da contagem do estoque
# Gera relatório com a quantidade de itens no estoque

# Aplicativo que Recebe a mensagem MQTT quando alguma mercadoria ENTRA ou SAI do estoque


import paho.mqtt.client as mqtt
import time

# callback que trata a menssagem recebida


def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))
    print("Tópico: " + str(message.topic))


# instancia o paho client
mqttBroker = "mqtt.eclipseprojects.io"
topic = "stock/in"
client = mqtt.Client("server")  # aqui pode inserir o clientName
msg = "Default message."

# conecta o client ao broker
client.connect(mqttBroker)

# precisamos subescrever um client que está em loop, então precisamos de um loop
client.loop_forever()
# Subescre o tópico
client.subscribe(topic)
# callback das mensagens
client.on_message = on_message
time.sleep(30)
client.loop_stop()
'''

def stock_controll(client, userdata, message):

    ITENS = []
    MESSAGE = str(message.payload.decode("utf-8"))

    # DO PYTHON 3.10 PRA CIMA, É POSSÍVEL USAR O MATCH/CASE PARA REALIZAR ESTA LÓGICA DE UMA FORMA MAIS LIMPA
    if messagem.topic == "StockIn":
        if MESSAGE == 1:
            ITENS[1] = ITENS[1] + 1
        elif MESSAGE == 2:
            ITENS[2] = ITENS[2] + 1
        elif MESSAGE == 3:
            ITENS[3] = ITENS[3] + 1
        else:
            print("No item called" + MESSAGE + "!")
    elif messagem.topic == "StockOut":
        if MESSAGE == 1:
            ITENS[1] = ITENS[1] - 1
        elif MESSAGE == 2:
            ITENS[2] = ITENS[2] - 1
        elif MESSAGE == 3:
            ITENS[3] = ITENS[3] - 1
        else:
            print("No item called" + MESSAGE + "!")'''
