# Write a Python program to read an entire text file.


def readFile(filename):
    with open(filename, "r") as file:
        print(file.read())


readFile("text.txt")
