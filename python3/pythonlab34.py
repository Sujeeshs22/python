# Write a Python program to get the file size of a plain file


import os


def file(fname):
    file = os.stat(fname)
    return file.st_size


print("File size= ", file("test.txt"))
