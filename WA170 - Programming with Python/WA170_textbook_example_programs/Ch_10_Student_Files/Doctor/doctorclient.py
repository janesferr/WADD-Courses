"""
File: doctorclient.py

Client for a therapy session.
"""

from socket import *
from codecs import decode

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
CODE = 'ascii'

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)
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
