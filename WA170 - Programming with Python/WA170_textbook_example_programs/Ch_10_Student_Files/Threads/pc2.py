import time, random
from threading import Thread, currentThread, Condition

class SharedCell(object):
    def __init__(self):
        self._data = -1
        self._writeable = True
        self._condition = Condition()

    def setData(self, data):
        self._condition.acquire()
        while not self._writeable:
            self._condition.wait()
        print("%s setting data to %d\n" % \
              (currentThread().getName(), data))
        self._data = data
        self._writeable = False
        self._condition.notify()
        self._condition.release()

    def getData(self):
        self._condition.acquire()
        while self._writeable:
            self._condition.wait()
        print("%s accessing data %d\n" % \
              (currentThread().getName(), self._data))
        self._writeable = True
        self._condition.notify()
        self._condition.release()
        return self._data

class Producer(Thread):

    def __init__(self, cell, accessCount, sleepInterval):
        Thread.__init__(self, name = "Producer")
        self._accessCount = accessCount
        self._cell = cell
        self._sleepInterval = sleepInterval

    def run(self):
        print("%s starting up\n" % self.getName())
        for count in range(self._accessCount):
            time.sleep(random.randint(1, self._sleepInterval))
            self._cell.setData(count + 1)
        print("%s is done producing\n" % self.getName())

class Consumer(Thread):

    def __init__(self, cell, accessCount, sleepInterval):
        Thread.__init__(self, name = "Consumer")
        self._accessCount = accessCount
        self._cell = cell
        self._sleepInterval = sleepInterval

    def run(self):
        print("%s starting up\n" % self.getName())
        for count in range(self._accessCount):
            time.sleep(random.randint(1, self._sleepInterval))
            value = self._cell.getData()
        print("%s is done consuming\n" % self.getName())

def main():
    accessCount = int(input("Enter the number of accesses: "))
    cell = SharedCell()
    p = Producer(cell, accessCount, 4)
    c = Consumer(cell, accessCount, 4)
    print("Starting the threads")
    p.start()
    c.start()

main()
