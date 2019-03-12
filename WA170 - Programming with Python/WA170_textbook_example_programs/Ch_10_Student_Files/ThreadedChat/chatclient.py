"""
Author: Ken Lambert

Client for a chat room
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
print server.recv(BUFSIZE)

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
