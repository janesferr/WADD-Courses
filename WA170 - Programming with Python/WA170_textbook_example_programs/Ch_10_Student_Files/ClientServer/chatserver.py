"""
Server for a chat room.  Handles one client at a 
time and participates in the conversation.
"""

from socket import *
from codecs import decode

HOST = 'localhost' 
PORT = 5000
ADDRESS = (HOST, PORT)
BUFSIZE = 1024
CODE = 'ascii'

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

while True:
    print('Waiting for connection . . .')
    client, address = server.accept()
    print('... connected from:', address)
    client.send(bytes('Welcome to my chat room!', CODE))   # Send greeting

    while True:
        message = decode(client.recv(BUFSIZE), CODE)       # Reply from client
        if not message:
            print('Client disconnected')
            client.close()
            break
        else:
            print(message) 
            client.send(bytes(input('> '), CODE))          # Reply to client

