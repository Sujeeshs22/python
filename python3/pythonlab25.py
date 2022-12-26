# Write a Python program to read first n lines of a file.

def readFirst(filename, n):
    with open(filename) as f:
        for line in (f.readlines()[:n]):
            print(line, end='')


readFirst("test.txt", 4)
