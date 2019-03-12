import time, random
from threading import Thread, currentThread

class SharedCell(object):
    def __init__(self):
        self._data = -1

    def setData(self, data):
        print("%s setting data to %d\n" % \
              (currentThread().getName(), data))
        self._data = data

    def getData(self):
        print("%s accessing data %d\n" % \
              (currentThread().getName(), self._data))
        return self._data

class Producer(Thread):

    def __init__(self, cell, accessCount, sleepMax):
        Thread.__init__(self, name = "Producer")
        self._accessCount = accessCount
        self._cell = cell
        self._sleepMax = sleepMax

    def run(self):
        print("%s starting up\n" % self.getName())
        for count in range(self._accessCount):
            time.sleep(random.randint(1, self._sleepMax))
            self._cell.setData(count + 1)
        print("%s is done producing\n" % self.getName())

class Consumer(Thread):

    def __init__(self, cell, accessCount, sleepMax):
        Thread.__init__(self, name = "Consumer")
        self._accessCount = accessCount
        self._cell = cell
        self._sleepMax = sleepMax

    def run(self):
        print("%s starting up\n" % self.getName())
        for count in range(self._accessCount):
            time.sleep(random.randint(1, self._sleepMax))
            value = self._cell.getData()
        print("%s is done consuming\n" % self.getName())

def main():
    accessCount = int(input("Enter the number of accesses: "))
    sleepMax = 4
    cell = SharedCell()
    p = Producer(cell, accessCount, sleepMax)
    c = Consumer(cell, accessCount, sleepMax)
    print("Starting the threads")
    p.start()
    c.start()

main()
