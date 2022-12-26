# Write a Python program to read a file line by line store it into a variable

def readFile(file):
    with open(file) as f:
        a = f.readlines()
        print(a)


readFile("test.txt")
