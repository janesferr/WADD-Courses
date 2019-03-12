"""
File: doctorserver.py
Project 10.7

Server for a therapy session.  Handles multiple clients
concurrently.

Loads doctor object from a file for an extisting patient.  When a
patient quits, saves the doctor object in a file.

The patient is asked for a username at login.  If a file named
<username>.dat exists, then that patient's doctor is loaded from
that file.  Otherwise, it's a new patient, for which a new doctor
is created.
"""

from socket import *
from codecs import decode
from threading import Thread
from doctor import Doctor
import os.path
import pickle

class ClientHandler(Thread):
    """Handles a session between a doctor and a patient."""
    def __init__(self, client):
        Thread.__init__(self)
        self._client = client

    def run(self):
        self._filename = decode(self._client.recv(BUFSIZE), CODE) + ".dat"
        if os.path.exists(self._filename):
            fileObj = open(self._filename, 'rb')
            self._dr = pickle.load(fileObj)
        else:
            self._dr = Doctor()
        self._client.send(bytes(self._dr.greeting(), CODE))
        while True:
            message = decode(self._client.recv(BUFSIZE), CODE)
            if not message:
                print('Client disconnected')
                self._client.close()
                fileObj = open(self._filename, 'wb')
                pickle.dump(self._dr, fileObj)
                break
            else:
                self._client.send(bytes(self._dr.reply(message), CODE))

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
    handler = ClientHandler(client)
    handler.start()
