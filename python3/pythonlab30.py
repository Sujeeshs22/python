# Write a Python program to read a file line by line store it into an array.


def readfile(filename):
    with open(filename) as file:
        li = file.readlines()
        print(li)


readfile("test.txt")
