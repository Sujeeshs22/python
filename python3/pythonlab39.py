# Write a Python program to remove newline characters from a file.

with open("text.txt", "r")as file:
    f = file.readlines()
    print([x.rstrip('\n')for x in f])
