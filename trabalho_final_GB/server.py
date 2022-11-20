# Aplicação do server.
# Recebe as mensagens MQTT e faz o incremento ou decremento da contagem do estoque
# Gera relatório com a quantidade de itens no estoque

# Aplicativo que Recebe a mensagem MQTT quando alguma mercadoria ENTRA ou SAI do estoque

import paho.mqtt.client as mqtt
import time


#controle de estoque
stockTotal=0
def stock_controll(client, userdata, message, MESSAGE):  
    global stockTotal
    # DO PYTHON 3.10 PRA CIMA, É POSSÍVEL USAR O MATCH/CASE PARA REALIZAR ESTA LÓGICA DE UMA FORMA MAIS LIMPA
    if message.topic == "stock/in":
        if MESSAGE == "1":
            stockTotal += 1
        elif MESSAGE == "2":
            stockTotal += 12
        elif MESSAGE == "3":
            stockTotal += 72
        else:
            print("No item packaging called " + MESSAGE + " !")
    elif message.topic == "stock/out":
        if MESSAGE == "1":
            stockTotal -= 1
        elif MESSAGE == "2":
            stockTotal -= 12
        elif MESSAGE == "3":
            stockTotal -= 72
        else:
            print("No item packaging called" + MESSAGE + "!")
    if stockTotal>=0:
        print("Current total units in stock is "+ str(stockTotal))  
        stockTotalGlobal=stockTotal
    else:
        print("Stock value cannot be less than zero.\nAn error occurred in the inventory count, check the actual quantity and update the system")  

# callback que trata a menssagem recebida

def on_message(client, userdata, message):
    MESSAGE = str(message.payload.decode("utf-8"))
    itemPackagingTypes= ["1","2","3"]
    embalagem = ""
    if (MESSAGE not in itemPackagingTypes):
        print("Received message:", MESSAGE)
        print("Topic: " + str(message.topic))
    if (MESSAGE in itemPackagingTypes):
        if MESSAGE == "1": embalagem= "Unity"
        elif MESSAGE == "2": embalagem= "Pack"
        elif MESSAGE == "3": embalagem= "Box"
        print("Item packaging:", embalagem)
        stock_controll(client, userdata, message, MESSAGE)


# instancia o paho client
mqttBroker = "mqtt.eclipseprojects.io"
topic = [("stock/in",0),("stock/out",0)]
msg = "Default message."

client = mqtt.Client("server")  # aqui pode inserir o clientName
# callback das mensagens
client.on_message = on_message
# conecta o client ao broker
client.connect(mqttBroker)

# Subescre o tópico
client.subscribe(topic)

try:
    print("Press CTRL+C to exit")
    client.loop_forever()

except:
    print("Disconnecting do broker.")

client.disconnect()


