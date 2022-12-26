# Write a Python program to count the frequency of words in a file.


from collections import Counter


def file(fname):
    with open(fname, 'r')as file:
        return Counter(file.read().split())


print(file("test.txt"))
