# Write a Python program to read a file line by line and store it into a list.


def readLine(file):
    with open(file)as f:
        li = f.readlines()
        print(li)


readLine('test.txt')
