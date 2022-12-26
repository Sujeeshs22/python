# Write a Python program to read last n lines of a file.


def readlast(filename, n):
    with open(filename)as file:
        for line in (file.readlines()[-n:]):
            print(line, end='')


readlast("text.txt", 2)
