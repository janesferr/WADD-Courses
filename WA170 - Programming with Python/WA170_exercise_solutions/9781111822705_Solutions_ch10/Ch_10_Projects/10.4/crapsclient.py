"""
File: crapsclient.py
Project 10.4

Client for a two-way craps game.

The client receives a greeting and then presses enter to
perform each roll.

The client receives the roll and then receives the
outcome.  Both are printed, and if the outcome is
"WIN" or "LOSE", the client quits.
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
    message = input('Press enter to roll the dice')
    server.send(bytes("ROLL", 'ascii'))
    roll = decode(server.recv(BUFSIZE), CODE)
    if not roll:
        print("Server disconnected")
        break
    print(roll)
    outcome = decode(server.recv(BUFSIZE), CODE)
    if not outcome:
        print("Server disconnected")
        break
    print("Outcome: " + outcome)
    if outcome == "WIN" or outcome == "LOSE":
        break
server.close()
