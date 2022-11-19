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
topic = "test/status"
client = mqtt.Client("server")  # aqui pode inserir o clientName
msg = "Default message."

# conecta o client ao broker
client.connect(mqttBroker)

# precisamos subescrever um client que está em loop, então precisamos de um loop
client.loop_start()
# Subescre o tópico
client.subscribe(topic)
# callback das mensagens
client.on_message = on_message
time.sleep(30)
client.loop_stop()