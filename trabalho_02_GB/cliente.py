import socket
import sys

#Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to the port
server_adress = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %d' %server_adress
sock.bind(server_adress)

#Listen for incoming connections
sock.listen(1)

while True:
    #Wait for a conection
    print >>sys.stderr, 'waiting for a connection'
    connection, clinet_address = sock.accept()

    try:
        print >>sys.stderr, 'connection from', clinet_address

        #Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' %data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', clinet_address
                break
    finally:
        #Clean ip the connection
        connection.close()
