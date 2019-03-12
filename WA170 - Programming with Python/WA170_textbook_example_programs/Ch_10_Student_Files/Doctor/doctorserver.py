"""
File: doctorserver.py

Server for a therapy session. Handles multiple clients
concurrently.
"""

from socket import *
from codecs import decode
from threading import Thread
from doctor import Doctor

class ClientHandler(Thread):
    """Handles a session between a doctor and a patient."""
    def __init__(self, client, dr):
        Thread.__init__(self)
        self._client = client
        self._dr = dr

    def run(self):
        self._client.send(bytes(self._dr.greeting(), 'ascii'))
        while True:
            message = decode(self._client.recv(BUFSIZE), 'ascii')
            if not message:
                print('Client disconnected')
                self._client.close()
                break
            else:
                self._client.send(bytes(self._dr.reply(message), 'ascii'))

HOST = 'localhost'
PORT = 21567
ADDRESS = (HOST, PORT)
BUFSIZE = 1024

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

while True:
    print('Waiting for connection . . .')
    client, address = server.accept()
    print('... connected from:', address)
    dr = Doctor()
    handler = ClientHandler(client, dr)
    handler.start()
