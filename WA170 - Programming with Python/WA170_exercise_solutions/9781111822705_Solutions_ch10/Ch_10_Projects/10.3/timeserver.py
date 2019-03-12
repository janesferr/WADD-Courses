"""
File: timeserver.py
Project 10.3

Server for providing the day and time.
Allows the server to be shut down gracefully.
Uses a thread for the server and waits for user
input to shut down.
"""

from socket import *
from time import ctime, sleep
from threading import Thread

class TimeServer(Thread):
    """Server for the day and time."""
    
    def __init__(self):
        """Includes Boolean flag to shut down."""
        Thread.__init__(self)
        self._done = False

    def run(self):
        """Runs until signaled to shut down.  At least
        one client must connect after the signal is sent."""
        HOST = 'localhost'
        PORT = 5000
        ADDRESS = (HOST, PORT)

        server = socket(AF_INET, SOCK_STREAM)
        server.bind(ADDRESS)
        server.listen(5)

        while not self._done:
            print('Waiting for connection . . .')
            client, address = server.accept()
            print('... connected from:', address)
            client.send(bytes(ctime() + '\nHave a nice day!', 'ascii'))
            client.close()

    def quit(self):
        """The server is signaled to shut down."""
        self._done = True

def main():
    """Starts the server thread and waits for the user to
    signal to quit."""
    server = TimeServer()
    server.start()
    input("Press enter to quit.")
    server.quit()
    print("Server shutting down.")

main()


