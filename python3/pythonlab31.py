# Write a python program to find the longest words.

def longest(filename):
    with open(filename, "r") as file:
        w = file.read().split()
        maxlen = len(max(w, key=len))
        return [x for x in w if len(w) == maxlen]


print(longest("test.txt"))
