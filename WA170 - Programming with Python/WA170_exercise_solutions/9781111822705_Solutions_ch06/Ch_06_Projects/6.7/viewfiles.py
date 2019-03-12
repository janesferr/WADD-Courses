"""
File: viewfiles.py
Project 6.7

Allows the user to visit all of the files in the current path and view them.

"""

import os, os.path

def main():
    displayFiles(os.getcwd())
    

def displayFiles(path):
    """Visits all of the files and directories in
    path and displays the files' contents."""
    if os.path.isfile(path):
        print("File name: " + path)
        f = open(path, 'r')
        print(f.read())
    else:
        print("Directory name: " + path)
        lyst = os.listdir(path)
        for element in lyst: displayFiles(element)

main()
