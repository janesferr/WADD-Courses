"""
File: doctorclient.py
Project 10.7

Client for a therapy session.

Sends a username to the server.
"""

from socket import *
from codecs import decode

HOST = 'localhost'
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
CODE = 'ascii'

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)
server.send(bytes(input("Enter your username: "), CODE))
print(decode(server.recv(BUFSIZE), CODE))

while True:
    message = input('> ')
    if not message:
        break
    server.send(bytes(message, CODE))
    reply = decode(server.recv(BUFSIZE), CODE)
    if not reply:
        print("Server disconnected")
        break
    print(reply)
server.close()
