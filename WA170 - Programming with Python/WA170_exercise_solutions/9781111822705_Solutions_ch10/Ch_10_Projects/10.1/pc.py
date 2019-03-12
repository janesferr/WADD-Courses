"""
File: pc.py
Project 10.1

Illustrates the producer/consumer problem with
thread synchronization.  Makes producer wait until multiple
consumers read each datum.
"""

import time, random
from threading import Thread, currentThread, Condition

class SharedCell(object):
    """Shared data for the producer/consumer problem."""

    # Includes a wait list of consumers who have thus far read data,
    # a second condition on which these consumers must wait, and
    # the maximum number of consumers who will read each datum.

    # The condition for synchonizing the producer with the consumers
    # does not change.

    # getData looks for the current thread in the wait list of
    # consumers.  If it's there, that consumer has already read the
    # current datum and must wait on the new condition.  Otherwise,
    # the consumer reads the datum and is placed on the wait wait list.
    # If the list becomes full, all of the consumers are finished with
    # the current datum, so they can all be notofied and the writer can
    # be released.
    
    def __init__(self, numConsumers):
        self._numConsumers = numConsumers
        self._waitList = []
        self._data = -1
        self._writeable = True
        self._condition = Condition()
        self._consumerCondition = Condition()

    def setData(self, data):
        """Producer's method to write to shared data."""
        self._condition.acquire()
        while not self._writeable:
            self._condition.wait()
        print("%s setting data to %d" % \
              (currentThread().getName(), data))
        self._data = data
        self._writeable = False
        self._condition.notify()
        self._condition.release()
        if len(self._waitList) == self._numConsumers:
            # Reset the wait list, release the writer, and
            # release all readers
            self._waitList = []
            self._consumerCondition.acquire()
            self._consumerCondition.notifyAll()
            self._consumerCondition.release()

    def getData(self):
        """Consumer's method to read from shared data."""
        # Wait on consumer condition if you have
        # already consumed this datum
        if currentThread() in self._waitList:
            self._consumerCondition.acquire()
            self._consumerCondition.wait()
        # Wait for writer to finish if datum has not been produced
        self._condition.acquire()
        while self._writeable:
            self._condition.wait()
        print("%s accessing data %d" % \
              (currentThread().getName(), self._data))
        # Check for releasing the producer and other consumers
        if len(self._waitList) == self._numConsumers - 1:
            # Reset the wait list, release the writer, and
            # release all readers
            self._waitList = []
            self._writeable = True
            self._consumerCondition.acquire()
            self._consumerCondition.notifyAll()
            self._consumerCondition.release()
        else:
            # More consumers, so go on wait list
            self._waitList.append(currentThread())
        self._condition.notify()
        self._condition.release()
        return self._data

class Producer(Thread):
    """Represents a producer."""

    def __init__(self, cell, accessCount, sleepMax):
        """Create a producer with the given shared cell,
        number of accesses, and maximum sleep interval."""
        Thread.__init__(self, name = "Producer")
        self._accessCount = accessCount
        self._cell = cell
        self._sleepMax = sleepMax

    def run(self):
        """Announce startup, sleep and write to shared cell
        the given number of times, and announce completion."""
        print("%s starting up\n" % self.getName())
        for count in range(self._accessCount):
            time.sleep(random.randint(1, self._sleepMax))
            self._cell.setData(count + 1)
        print("%s is done producing\n" % self.getName())

class Consumer(Thread):
    """Represents a consumer."""

    def __init__(self, name, cell, accessCount, sleepMax):
        """Create a consumer with the given shared cell,
        number of accesses, and maximum sleep interval."""
        Thread.__init__(self, name = "Consumer " + name)
        self._accessCount = accessCount
        self._cell = cell
        self._sleepMax = sleepMax

    def run(self):
        """Announce startup, sleep and read from shared cell
        the given number of times, and announce completion."""
        print("%s starting up\n" % self.getName())
        for count in range(self._accessCount):
            time.sleep(random.randint(1, self._sleepMax))
            value = self._cell.getData()
        print("%s is done consuming\n" % self.getName())

def main():
    """Get numberof accesses from the user, create a shared cell,
    and create and start up a producer and a consumer."""
    numConsumers = int(input("Enter the number of consumers: "))
    accessCount = int(input("Enter the number of accesses: "))
    cell = SharedCell(numConsumers)
    p = Producer(cell, accessCount, 4)
    consumers = []
    for count in range(numConsumers):
        consumers.append(Consumer(str(count), cell, accessCount, 4))
    print("Starting the threads")
    p.start()
    for c in consumers:
        c.start()

main()
