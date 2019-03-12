"""
File: registration.py
Project 10.1

Assigns concurrent student requests for course sections.
There are 5 sections with 20 seats each, and 100 student
threads requsting a seat.
"""

import time, random
from threading import Thread, currentThread, Condition

class Course(object):
    """Represents a shared course with 5 sections of 20 students each."""

    MAX_ENROLLMENT = 20
    
    def __init__(self):
        self._sections = [0, 0, 0, 0, 0]
        self._writeable = True
        self._condition = Condition()

    def register(self):
        """Assigns a seat in a section and returns the section number."""
        # Acquire the condition and wait if not writeable
        self._condition.acquire()
        while not self._writeable:
            self._condition.wait()
        # Enter the critical section
        self._writeable = False
        mySectionNumber = 1000            # Never assigned, but check for errors
        for sectionNumber in range(5):
            if self._sections[sectionNumber] < Course.MAX_ENROLLMENT:
                self._sections[sectionNumber] = self._sections[sectionNumber] + 1
                mySectionNumber = sectionNumber + 1
                break
        # Signal the other threads and release the condition
        self._writeable = True
        self._condition.notify()
        self._condition.release()
        return mySectionNumber
                
class Student(Thread):

    def __init__(self, course, name, sleepInterval):
        Thread.__init__(self, name = name)
        self._course = course
        self._sleepInterval = sleepInterval

    def run(self):
        print("%s starting up\n" % self.getName())
        time.sleep(random.randint(1, self._sleepInterval))
        sectionNumber = self._course.register()
        print("%s has been assigned to section %d\n" % (self.getName(), sectionNumber))

def main():
    # Create the shared course object
    course = Course()
    # Create the 100 student threads
    students = []
    for count in range(100):
        students.append(Student(course,
                                "Student " + str(count + 1),
                                random.randint(1, 4)))
    print("Starting the threads")
    for student in students:
        student.start()
              
main()
