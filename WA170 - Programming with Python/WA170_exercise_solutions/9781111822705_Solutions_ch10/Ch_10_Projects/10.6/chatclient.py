"""
File: chatclient.py
Project 10.6

Client for a multi-ciient chat room.
Allows the user to request the record of the chat.
To do this, the user enters the command RECEIVE.
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
print(decode(server.recv(BUFSIZE), CODE))
name = input('Enter your name: ')
server.send(bytes(name, CODE))

while True:
    record = decode(server.recv(BUFSIZE), CODE)
    if not record:
        break
    print(record)
    print("Enter RECEIVE to view the chat record, or just enter text.")
    message = input('> ')
    if not message:
        print("Server disconnected")
        break
    server.send(bytes(message, CODE))
server.close()
