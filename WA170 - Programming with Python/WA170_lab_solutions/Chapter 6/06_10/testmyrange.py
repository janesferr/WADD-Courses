"""
File: testmyrange.py
Project 6.10

Defines a function that behaves like Python's range function.

"""
    

def myRange(start, stop = None, step = None):
    lyst = []
    if stop == None and step == None:
        stop = start
        start = 0
        step = 1
    if start < stop:
        if step == None:
            step = 1
        elif step <= 0:
            return lyst
        while start < stop:
            lyst.append(start)
            start += step
    else:
        if step == None or step > -1:
            return lyst
        while start > stop:
            lyst.append(start)
            start += step
    return lyst
            
def main():
    print(myRange(10))
    print(myRange(1, 10))
    print(myRange(1, 10, 2))
    print(myRange(10, 1, -1))

main()

