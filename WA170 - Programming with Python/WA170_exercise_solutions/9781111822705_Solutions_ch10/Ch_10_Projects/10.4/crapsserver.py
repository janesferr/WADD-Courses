"""
File: crapsserver.py
Project 10.4

Server for a two-way craps game.

This server can handle multiple clients in games.
"""

from socket import *
from codecs import decode
from threading import Thread
from player import Player

class ClientHandler(Thread):
    """Plays a game with a client."""
    
    def __init__(self, client):
        Thread.__init__(self)
        self._client = client
        self._clientPlayer = Player()
        self._serverPlayer = Player()

    def run(self):
        self._client.send(bytes('Welcome to the craps game!', CODE))
        while True:
            message = decode(self._client.recv(BUFSIZE), CODE)
            if not message:
                print('Client disconnected')
                self._client.close()
                break
            else:
                clientOutcome = self._clientPlayer.roll()
                clientRoll = "Your roll: " + str(self._clientPlayer)
                if clientOutcome == "CONTINUE":
                    serverOutcome = self._serverPlayer.roll()
                    serverRoll = str(self._serverPlayer)
                    if serverOutcome == "WIN":
                        clientOutcome = "LOSE"
                    elif serverOutcome == "LOSE":
                        clientOutcome = "WIN"
                    clientRoll = clientRoll + \
                                 "My roll  : " + serverRoll
                self._client.send(bytes(clientRoll, CODE))
                self._client.send(bytes(clientOutcome, CODE))
                if clientOutcome in ("WIN", "LOSE"):
                    print('Game over')
                    self._client.close()
                    break

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


