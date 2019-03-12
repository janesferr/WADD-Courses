"""
Author: Ken Lambert

Server for a chat room
"""

from socket import *
from codecs import decode
from threading import Thread

class ClientHandler(Thread):
    
    def __init__(self, client):
        Thread.__init__(self)
        self._client = client

    def run(self):
        self._client.send(bytes('Welcome to my chat room!', CODE))
        while True:
            message = decode(self._client.recv(BUFSIZE), CODE)
            if not message:
                print('Client disconnected')
                self._client.close()
                break
            else:
                print message 
                self._client.send(bytes(input('> '), CODE))
        

HOST = 'localhost'
PORT = 21567
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
    ClientHandler(client).start()

server.close()


