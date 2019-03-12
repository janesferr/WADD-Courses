"""
File: timeclient.py
Project 10.3

Client for obtaining the day and time.
"""

from socket import *
from codecs import decode

HOST = 'localhost' 
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)   # Create a socket
server.connect(ADDRESS)                 # Connect it to a host
dayAndTime = server.recv(BUFSIZE)       # Read a string from it
print(decode(dayAndTime, 'ascii'))
server.close()                          # Close the connection
